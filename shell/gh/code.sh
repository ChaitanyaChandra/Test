#!/bin/bash

# Both TIMESTAMP and HOSTNAME are injected as env variables from workflow steps

TABLE_TYPE="${1:-RESOURCE}"

if [[ "$OSTYPE" == "darwin"* ]]; then
  cpus=$(sysctl -n hw.ncpu)
  mem_bytes=$(sysctl -n hw.memsize)
  memory="$((mem_bytes / 1024 / 1024 / 1024)) GB"
else
  cpus=$(nproc)
  memory=$(free -h | awk '/^Mem:/ {print $2}')
fi

# Set the rows and title based on the table type
if [[ "$TABLE_TYPE" == "RESOURCE" ]]; then
  title="RESOURCE"
  rows=("CPUs:'$cpus'" "Memory:'$memory'")
elif [[ "$TABLE_TYPE" == "STATUS" ]]; then
  title="STATUS"
  rows=("Hostname:'$HN'" "Timestamp:'$TIMESTAMP'")
else
  echo "Error: Unknown table type '$TABLE_TYPE'" >&2
  exit 1
fi

# Generic Table
summary="# $title"
summary+=$'\n| Item   | Data                    | Status  |'
summary+=$'\n|--------|-------------------------|---------|'
for item in "${rows[@]}"; do
  name="${item%%:*}"
  val="${item#*:}"
  summary+=$'\n'"| $name | $val | Success |"
done
printf '%s\n\n' "$summary" >> "$GITHUB_STEP_SUMMARY"

echo "✅ $title summary written"
