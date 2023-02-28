#!/usr/bin/env bash

echo "The PATH is: $PATH"
echo "The terminal is: $TERM"
echo "The editor is $EDITOR"
echo "The home is $HOME"
echo "The hostname is $HOSTNAME"
echo "The shell is $SHELL"
echo "The user is $USER"
if [ -z $EDITOR]
then
    echo "The EDITOR variable is not set"
fi