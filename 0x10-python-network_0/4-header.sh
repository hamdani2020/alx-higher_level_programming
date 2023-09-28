#!/bin/bash
# It takes in a URL as an argument and displays response body
curl -s "$1" -X GET -H "X-School-User-Id: 98"
