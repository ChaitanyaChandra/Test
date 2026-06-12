#!/bin/bash

# Both TIMESTAMP and HOSTNAME are injected as env variables from workflow steps

summary=$'# STATUS'
summary+=$'\n| Item      | Data                    | Status  |'
summary+=$'\n|-----------|-------------------------|---------|'
summary+=$'\n'"| Timestamp | '$TIMESTAMP'            | Success |"
summary+=$'\n'"| Hostname  | '$HN'                   | Success |"

printf '%s\n' "$summary" >> "$GITHUB_STEP_SUMMARY"

echo "✅ Summary written — Timestamp=$TIMESTAMP  Hostname=$HN"
