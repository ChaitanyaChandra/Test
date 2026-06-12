#!/bin/bash


summary=$'# STATUS'
summary+=$'\n| Item | Data | Status |'
summary+=$'\n|-----|------|--------|'

time=$(date '+%Y-%m-%d %H:%M:%S')
summary+=$'\n'"| Timestamp | '$time' | Success |"

printf '%s\n' "$summary" >> "$GITHUB_STEP_SUMMARY"
