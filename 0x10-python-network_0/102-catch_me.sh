#!/bin/bash
#make request to 0.0.0.:5000/catch_me, server respond with msg "You got me!"
curl -x -X PUT -d "user_id=98" -L -H "Origin: HolbertonSchool" 0.0.0.0:5000/catch_me
