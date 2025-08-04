docker build -t docker.io/chaitanyachandra/awx-operator:2.19.1 -t docker.io/chaitanyachandra/awx-operator:latest .
docker push docker.io/chaitanyachandra/awx-operator:2.19.1
docker push docker.io/chaitanyachandra/awx-operator:latest

docker build -t docker.io/chaitanyachandra/kube-rbac-proxy:v0.15.0  -t docker.io/chaitanyachandra/kube-rbac-proxy:latest .
docker push docker.io/chaitanyachandra/kube-rbac-proxy:v0.15.0
docker push docker.io/chaitanyachandra/kube-rbac-proxy:latest