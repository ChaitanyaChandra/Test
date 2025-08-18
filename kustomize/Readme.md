### Helm

```shell
# create new template
helm create spec-app

# generate yaml files form template 
kubectl kustomize  overlays/prod  > test.yaml 
kustomize build overlays/prod

# install
k apply -k overlays/prod

# delete 
k delete -k overlays/prod

# update
helm upgrade spec spec-app -n test

# history 
helm history spec -n test


# rollback
helm rollback spec -n test 5
```