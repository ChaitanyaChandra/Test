#!/bin/bash

# Both TIMESTAMP and HOSTNAME are injected as env variables from workflow steps

if [[ "$OSTYPE" == "darwin"* ]]; then
  cpus=$(sysctl -n hw.ncpu)
  mem_bytes=$(sysctl -n hw.memsize)
  memory="$((mem_bytes / 1024 / 1024 / 1024)) GB"
else
  cpus=$(nproc)
  memory=$(free -h | awk '/^Mem:/ {print $2}')
fi

# Resource Table
summary=$'# RESOURCE'
summary+=$'\n| Item   | Data                    | Status  |'
summary+=$'\n|--------|-------------------------|---------|'
summary+=$'\n'"| CPUs   | '$cpus'                 | Success |"
summary+=$'\n'"| Memory | '$memory'               | Success |"

summary+=$'\n\n'

# Status Table
summary+=$'# STATUS'
summary+=$'\n| Item      | Data                    | Status  |'
summary+=$'\n|-----------|-------------------------|---------|'
summary+=$'\n'"| Hostname  | '$HN'                   | Success |"
summary+=$'\n'"| Timestamp | '$TIMESTAMP'            | Success |"

printf '%s\n' "$summary" >> "$GITHUB_STEP_SUMMARY"

echo "✅ Resource and Status summaries written — CPUs=$cpus Memory=$memory Hostname=$HN Timestamp=$TIMESTAMP"
