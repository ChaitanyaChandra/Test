# Generate private key
openssl genrsa -out webhook-server.key 2048

# https://master.chaitu.net:5555/mutate?timeout=5s

# Generate a CSR
openssl req -new -key webhook-server.key -subj "/CN=master.chaitu.net" -out webhook-server.csr

# Generate a self-signed CA
openssl req -x509 -newkey rsa:4096 -sha256 -days 10000 -nodes \
  -keyout ca.key -out ca.crt -subj "/CN=webhook-ca"

# Create a CSR config file for SAN (Subject Alternative Names)
cat <<EOF > csr.conf
[ req ]
default_bits = 2048
prompt = no
default_md = sha256
distinguished_name = dn
req_extensions = v3_req

[ dn ]
CN = master.chaitu.net

[ v3_req ]
subjectAltName = @alt_names

[ alt_names ]
DNS.1 = master.chaitu.net
DNS.2 = webhook-service
DNS.3 = webhook-service.webhook
DNS.4 = webhook-service.webhook.svc
EOF

# Sign the webhook server CSR with the CA
openssl x509 -req -in webhook-server.csr \
  -CA ca.crt -CAkey ca.key -CAcreateserial \
  -out webhook-server.crt -days 10000 -sha256 \
  -extensions v3_req -extfile csr.conf

# mv cert and key as tls.crt and tls.key
mv webhook-server.crt tls.crt
mv webhook-server.key tls.key

# Encode CA cert for kubernetes webhook YAML
cat ca.crt | base64 | tr -d '\n' > ca_bundle.txt


kubectl create secret tls webhook-tls-secret \
  --cert=tls.crt \
  --key=tls.key \
  -n webhook

docker rmi $(docker images -a -q ) --force

docker build -t docker.io/chaitanyachandra/webhook:arm_1.0  -t docker.io/chaitanyachandra/webhook:arm_latest .
docker push docker.io/chaitanyachandra/webhook:arm_1.0
docker push docker.io/chaitanyachandra/webhook:arm_latest

docker run -d \
  -p 5555:8080 \
  -v ./CA/tls.crt:/mnt/certs/tls.crt:ro \
  -v ./CA/tls.key:/mnt/certs/tls.key:ro \
  --name webhook-app \
  chaitanyachandra/webhook:arm_latest

curl -k -X POST https://master.chaitu.net:5555/mutate \
  -H "Content-Type: application/json" \
  --data @test.json



kubectl run webhook-pod --image=chaitanyachandra/webhook:arm_3.0 -it --rm -- /bin/sh


uvicorn --host 0.0.0.0 --port 5555 index:app --ssl-keyfile ../CA/tls.key --ssl-certfile ../CA/tls.crt

curl --resolve master.chaitu.net:5555:129.159.23.81 \
  --cacert CA/ca.crt \
  -X POST https://master.chaitu.net:5555/validate-rewrite/validate \
  -H "Content-Type: application/json" \
  --data @test/re-write-test.json

curl --resolve master.chaitu.net:5555:129.159.23.81 \
  --cacert CA/ca.crt \
  -X POST https://master.chaitu.net:5555/requests-limits/mutate \
  -H "Content-Type: application/json" \
  --data @test/deploy-test.json



# {"apiVersion":"admission.k8s.io/v1","kind":"AdmissionReview","response":{"uid":"67890","allowed":false,"warnings":["'nginx.ingress.kubernetes.io/rewrite-target: /name$1,age=$2' must not contain values like $1, $2, etc."]}}

mysql -e "
CREATE TABLE c_logs (
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    cluster_name VARCHAR(255) NOT NULL,
    namespace VARCHAR(255) NOT NULL,
    deployment VARCHAR(255) NOT NULL,
    container VARCHAR(255) NOT NULL,
    cpu INT NOT NULL,
    memory INT NOT NULL,
    log_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
);
"

mysql -e "
INSERT INTO c_logs
    (cluster_name, namespace, deployment, container, cpu, memory)
VALUES
    ('master', 'chaitanya-chandra-testing', 'demo-deployment-1', 'demo-container', 450, 249),
    ('master', 'chaitanya-chandra-testing', 'demo-deployment-2', 'demo-container', 500, 250),
    ('master', 'chaitanya-chandra-testing', 'demo-deployment-2', 'demo-container-two', 600, 256);
"