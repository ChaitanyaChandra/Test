docker build -t docker.io/chaitanyachandra/awx-operator:2.19.1 -t docker.io/chaitanyachandra/awx-operator:latest .
docker push docker.io/chaitanyachandra/awx-operator:2.19.1
docker push docker.io/chaitanyachandra/awx-operator:latest

docker build -t docker.io/chaitanyachandra/kube-rbac-proxy:v0.15.0  -t docker.io/chaitanyachandra/kube-rbac-proxy:latest .
docker push docker.io/chaitanyachandra/kube-rbac-proxy:v0.15.0
docker push docker.io/chaitanyachandra/kube-rbac-proxy:latest


docker build -t docker.io/chaitanyachandra/app:1.0  -t docker.io/chaitanyachandra/app:latest .
docker push docker.io/chaitanyachandra/app:1.0
docker push docker.io/chaitanyachandra/app:latest

kubectl create secret docker-registry regcred \
  --docker-server=https://index.docker.io/v1/ \
  --docker-username=<your-dockerhub-username> \
  --docker-password=<your-dockerhub-password> \
  --docker-email=<your-email> \
  -n awx