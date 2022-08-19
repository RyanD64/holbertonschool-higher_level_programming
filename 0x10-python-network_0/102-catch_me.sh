#!/bin/bash
# Bash script that takes in a URL
curl -s -X PUT -L  -H "Origin:HolbertonSchool" "0.0.0.0:5000/catch_me" -d "user_id=98"
