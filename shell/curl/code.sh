#!/bin/bash

while read -r domain port
do
    [[ -z "$domain" || "$domain" == \#* ]] && continue

    if kubectl exec -n default debug -- nc -vz -w 5 "$domain" "$port" </dev/null &>/dev/null; then
        echo "$domain:$port --> Connected"
    else
        echo "$domain:$port --> TIMEOUT"
    fi

done < file.txt

