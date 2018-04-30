#!/bin/bash
nohup python -m trip.app > /dev/null 2>&1 &
tail --retry -f -n 0 ./logs/info.log ./logs/error.log
