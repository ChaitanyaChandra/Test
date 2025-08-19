### Helm

```shell
# create new template
helm create spec-app

# generate yaml files form template 
kubectl kustomize  overlays/prod  > test.yaml 
kustomize build overlays/prod

# install
k apply -k overlays/prod
kustomize build overlays/prod | k apply -f -

# delete 
k delete -k overlays/prod
kustomize build overlays/prod | k delete -f -
# update

# history 


# rollback
```