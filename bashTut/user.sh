#!/usr/bin/env bash

VALID=0

while [ $VALID -eq 0 ]
do
    read -p "Please enter you name and age: " NAME AGE
    if [[ (-z $NAME ) || ( -z $AGE ) ]]
    then
        echo "Not enough parameters passed"
        continue
    elif [[ ! $NAME =~ ^[A-Za-z]+$ ]]
    then
        echo "Non alpha characters detected [$NAME]"
        continue
    elif [[ ! $AGE =~ ^[0-9]+$ ]]
    then
        echo "None digit chatacters detected [$AGE]"
        continue
    fi
    VALID=1
done
echo "Name = $NAME and Age = $AGE"