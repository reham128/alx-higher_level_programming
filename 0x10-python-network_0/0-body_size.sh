#!/bin/bash
#script to take URL, send request to that URL,display size of body respon
curl -s "$1" | wc -c
