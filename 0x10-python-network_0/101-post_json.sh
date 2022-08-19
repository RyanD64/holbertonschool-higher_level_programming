#!/bin/bash
# Bash script that takes in a URL
curl -s "$1" -X POST -d "@$2" -H "Content-Type: application/json"
