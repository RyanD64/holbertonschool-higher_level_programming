#!/bin/bash
# Bash script that takes in a URL
curl -s -o /dev/null -w "%{http_code}" "$1"