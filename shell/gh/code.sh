#!/bin/bash

summary=$'# STATUS'
summary+=$'\n| Item | Data | Status |'
summary+=$'\n|-----|------|--------|'

time=$(date '+%Y-%m-%d %H:%M:%S')
hn=$(hostname)

summary+=$'\n'"| Timestamp | '$time' | Success |"
summary+=$'\n'"| Hostname | '$hn' | Success |"


echo -e "$summary" >> "$GITHUB_STEP_SUMMARY"

# Expose this step's summary file path so other steps can append to it
echo "summary_file=$GITHUB_STEP_SUMMARY" >> "$GITHUB_OUTPUT"
