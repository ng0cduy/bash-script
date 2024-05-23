#!/usr/bin/env bash

RANDOM_NUMBER=25

STATE=1

while [ $STATE -eq 1 ]
do
    read -p "INPUT THE RANDOM NUMBER " NUMBER
    if [ $NUMBER -lt $RANDOM_NUMBER ]
    then
        echo "The number is too low "
    elif [ $NUMBER -gt $RANDOM_NUMBER ]
    then
        echo "The number is too high "
    elif [ $NUMBER -eq $RANDOM_NUMBER ]
    then
        echo "Bingo. You got it "
        STATE=0
    fi
done
