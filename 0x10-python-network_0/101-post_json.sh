#!/bin/bash
#script to send json POST request to URL with given json file
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
