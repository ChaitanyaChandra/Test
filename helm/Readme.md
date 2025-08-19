### Helm

```shell
# create new template
helm create spec-app

# generate yaml files form template 
helm install spec -n test spec-app --dry-run > test.yaml 

# install
helm install spec -n test spec-app

# delete 
helm delete spec -n test 

# update
helm upgrade spec -n test

# history 
helm list -n test
helm history spec -n test


# rollback
helm rollback spec -n test 5
```