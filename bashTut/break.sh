#!/usr/bin/env bash

NAME=$@

for Name in $NAME
do
    if [ $Name = "Tracy" ]
    then
        continue
    fi
    echo "Hello $Name"
done

echo "for loop end"

exit 0