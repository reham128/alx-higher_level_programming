#!/bin/bash
# takes in a URL, send POST request to passed URL, display body response
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
