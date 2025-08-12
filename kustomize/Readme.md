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
helm upgrade spec spec-app -n test

# history 
helm history spec -n test


# rollback
helm rollback spec -n test 5
```