#!/bin/bash

echo $(dirname $0)

python3 -m pip install requests

cd $(dirname $0)/scripts/

python3 flightfocus365.py > ../flightfocus365.m3u8

echo m3u8 grabbed
