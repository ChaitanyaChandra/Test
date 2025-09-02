k get deploy  -o json -A | jq -r '.items[] |  "name:  \(.metadata.name) namespace:  \(.metadata.namespace)"'
k get po -A -o json | jq -r '.items[] | "\(.metadata.name) --- \(.status.qosClass) --- \(.spec.containers[].resources)"'

k exec -it debug -- sh -c '
TOKEN=$(cat /var/run/secrets/kubernetes.io/serviceaccount/token)
CACERT="/var/run/secrets/kubernetes.io/serviceaccount/ca.crt"
curl --cacert ${CACERT} https://kubernetes.default/api/v1/pods -H "Authorization: Bearer ${TOKEN}"' > out.txt

k auth can-i get po --as system:serviceaccount:default:debug-sa

k config view --raw -o json | jq -r '.users[0].user["client-certificate-data"]' | base64 -d |openssl x509  --text -noout | grep Validity -a3

k get po -A -o jsonpath="{range .items[*]} {.metadata.name} {.status.qosClass} {.spec.containers[*].resources} {'\n'}"

