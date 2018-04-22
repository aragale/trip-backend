#!/bin/bash
nohup python3 -m trip.main > /dev/null 2>&1 &
tail -f -n 0 ./logs/info.log ./logs/error.log
