#!/bin/bash
# It sends JSON post request
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
