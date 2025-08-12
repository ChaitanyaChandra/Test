# Generate private key
openssl genrsa -out webhook-server.key 2048

# Generate a CSR
openssl req -new -key webhook-server.key -subj "/CN=webhook-app.webhook.svc.svc.durgasri.in" -out webhook-server.csr

# Generate a self-signed CA
openssl req -x509 -newkey rsa:4096 -sha256 -days 10000 -nodes -keyout ca.key -out ca.crt -subj "/CN=webhook-app.webhook.svc.svc.durgasri.in"

# Sign the webhook server CSR with the CA
openssl x509 -req -in webhook-server.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out webhook-server.crt -days 10000 -sha256

# mv cert and key as tls.crt and tls.key
mv webhook-server.crt tls.crt
mv webhook-server.key tls.key

# Encode CA cert for kubernetes webhook YAML
cat ca.crt | base64 | tr -d '\n' > ca_bundle.txt
