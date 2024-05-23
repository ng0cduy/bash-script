#!/usr/bin/env bash

COUNT=0

while [ $COUNT -le 20 ]
do
    echo "Count = $COUNT"
    ((COUNT++))
done

echo "While loop finish"