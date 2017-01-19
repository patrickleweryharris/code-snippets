#!/bin/bash
while IFS='' read -r line || [[ -n "$line" ]]; do
    youtube-dl $line
done <"$1"
