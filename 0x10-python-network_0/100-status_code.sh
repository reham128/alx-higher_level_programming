#!/bin/bash
#script to send request to URL passed as argument, displays only status
curl -so /dev/null -w "%{http_code}" "$1"
