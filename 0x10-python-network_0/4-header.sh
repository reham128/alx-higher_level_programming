#!/bin/bash
#takes in URL as arg, send GET request to URL, display body of respons
curl -sH "X-School-User-Id: 98" "$1"
