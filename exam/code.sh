k get deploy  -o json -A | jq -r '.items[] |  "name:  \(.metadata.name) namespace:  \(.metadata.namespace)"'
k get po -A -o json | jq -r '.items[] | "\(.metadata.name) --- \(.status.qosClass) --- \(.spec.containers[].resources)"'

k exec -it debug -- sh -c '
token=$(cat /var/run/secrets/kubernetes.io/serviceaccount/token)
curl -k https://kubernetes.default/api/v1/pods -H "Authorization: Bearer $token"' > out.txt


