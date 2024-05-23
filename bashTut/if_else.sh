#!/usr/bin/env bash

COLOR=$1

if [ $COLOR = 'blue' ]
then
    echo 'The color is blue'
else
    echo 'The color are not blue'
fi

USER_GUESS=$2
COMPUTER=50
# boolean compares -eq , -ne, -lt , -gt , -le , -ge
if [ $USER_GUESS -lt $COMPUTER ]
then
    echo "You are too low"
elif [ $USER_GUESS -eq $COMPUTER ]
then
    echo "You are equal"
else
    echo "You are too high"
fi