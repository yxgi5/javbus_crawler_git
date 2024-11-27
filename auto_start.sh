#!/bin/bash

for line in $(cat tmp.list)
do
    if [ -e /usr/bin/python3.8 ]; then
        python3.8 crawler.py $line
    else
        python3 crawler.py $line
    fi
done



