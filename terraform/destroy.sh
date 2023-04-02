#!/bin/bash

# Define a list of items
apps=("nodejs" "java")

# Loop through the list and print each item
for app in "${apps[@]}"
do
    terraform destroy --target module.$app.module.blue  --auto-approve
done