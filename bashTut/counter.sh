#!/usr/bin/env bash

NUMBER=$1
COUNT=1
while [ $COUNT -le $NUMBER ]
do
    echo $COUNT
    ((COUNT++))
done
echo "end of while loop"