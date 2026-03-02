openssl genrsa -out ca.key 4096
openssl req -x509 -new -nodes \
  -key ca.key \
  -sha256 \
  -days 3650 \
  -out ca.crt \
  -subj "/C=IN/ST=AP/L=Nellore/O=Chaitanya/OU=K8S/CN=chaitanya"
openssl x509 -in ca.crt -text -noout

kubectl create secret tls root-ca-secret \
  --cert=ca.crt \
  --key=ca.key \
  -n chaitanya