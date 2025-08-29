k create sa durgasri-sa -n dev

kubectl apply -f - <<EOF
apiVersion: v1
kind: Secret
metadata:
  name: durgasri-sa-token
  namespace: dev
  annotations:
    kubernetes.io/service-account.name: durgasri-sa
type: kubernetes.io/service-account-token
EOF


# kubectl create token durgasri-sa -n dev --duration=8760h
kubectl create clusterrole durgasri-cr --verb=get,list,watch --resource=pods,pods/status
kubectl create clusterrolebinding durgasri-crb --clusterrole=durgasri-cr --serviceaccount=dev:durgasri-sa

cat > "$HOME/.kube/chay/config" <<EOF
apiVersion: v1
clusters:
- cluster:
    certificate-authority-data: $(cat $HOME/.kube/ca/main.crt | base64 | tr -d '\n') #$(k get secrets -n dev  durgasri-sa-token -o json  | jq -r '.data."ca.crt"')
    server: https://kubernetes.default.svc.svc.durgasri.in:16443/
  name: kubernetes
contexts:
- context:
    cluster: kubernetes
    user: user1
  name: user1@kubernetes
current-context: user1@kubernetes
kind: Config
preferences: {}
users:
- name: user1
  user:
    token: $(k get secrets -n dev  durgasri-sa-token -o json  | jq -r '.data.token' |  base64 -d)
EOF