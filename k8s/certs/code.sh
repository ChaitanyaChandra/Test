cat <<EOF | cfssl genkey - | cfssljson -bare server
{
  "hosts": [
    "*.durgasri.in"
  ],
  "CN": "durgasri",
  "key": {
    "algo": "ecdsa",
    "size": 256
  }
}
EOF

cat <<EOF | kubectl apply -f -
apiVersion: certificates.k8s.io/v1
kind: CertificateSigningRequest
metadata:
  name: durgasri
spec:
  request: $(cat server.csr | base64 | tr -d '\n')
  signerName: kubernetes.io/kube-apiserver-client
  usages:
  - digital signature
  - key encipherment
  - client auth
EOF

k certificate approve durgasri

scp cp:/etc/kubernetes/pki/ca.crt ~/.kube/ca/main.crt

kubectl get csr durgasri -o jsonpath='{.status.certificate}' | base64 -d > server.crt


cat > "$HOME/.kube/chay/config"  <<EOF
apiVersion: v1
clusters:
- cluster:
    certificate-authority-data: $(cat $HOME/.kube/ca/main.crt | base64 | tr -d '\n')
    server: https://kubernetes.default.svc.svc.durgasri.in:16443/
  name: kubernetes
contexts:
- context:
    cluster: kubernetes
    user: kubernetes-admin
  name: kubernetes-admin@kubernetes
current-context: kubernetes-admin@kubernetes
kind: Config
preferences: {}
users:
- name: kubernetes-admin
  user:
    client-certificate-data: $(cat server.crt | base64 | tr -d '\n')
    client-key-data: $(cat server-key.pem | base64 | tr -d '\n')
EOF

kubectl create role durgasri --verb=get,list,watch --resource=pods,pods/status -n test
kubectl create rolebinding durgasri-admin-binding --clusterrole=admin --user=durgasri --namespace=test
