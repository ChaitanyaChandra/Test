#!/bin/bash
set +x
echo "::add-mask::$MASK_VAL"
echo "data_hex=$MASK_VAL" >> "$GITHUB_ENV"
