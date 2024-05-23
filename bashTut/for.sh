#!/usr/bin/env bash

NAME=$@

for Name in $NAME
do
    echo "Hello $Name"
done

echo "for loop end"
exit 0