#!/bin/bash
while IFS='' read -r line || [[ -n "$line" ]]; do
    you-get --no-caption $line
done < "$1"
