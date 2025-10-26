# Generate private key
openssl genrsa -out webhook-server.key 2048

# https://webhook-service.webhook.svc:443/mutate?timeout=5s

# Generate a CSR
openssl req -new -key webhook-server.key -subj "/CN=webhook-service.webhook.svc" -out webhook-server.csr

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
CN = webhook-service.webhook.svc

[ v3_req ]
subjectAltName = @alt_names

[ alt_names ]
DNS.1 = webhook-service
DNS.2 = webhook-service.webhook
DNS.3 = webhook-service.webhook.svc
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

docker build -t docker.io/chaitanyachandra/webhook:arm_2.0  -t docker.io/chaitanyachandra/webhook:arm_latest .
docker push docker.io/chaitanyachandra/webhook:arm_2.0
docker push docker.io/chaitanyachandra/webhook:arm_latest



kubectl run webhook-pod --image=chaitanyachandra/webhook:arm_2.0 -it --rm -- /bin/sh
