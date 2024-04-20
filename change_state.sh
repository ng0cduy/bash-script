#!/bin/bash -x
source function.sh
set -e
change_state_file="change_state_list.txt"
current=$1
current_file="phase/phase$current/phase$current.txt"
while IFS= read -r line
do
    replace_line_number=$(cat $current_file | grep -n $line | cut -d: -f1)
    if [ -n $replace_line_number ]
    then
        sed -i "$replace_line_number s/,NA,/,JP,/" $current_file
        sed -n "$replace_line_number p" $current_file
    fi
done < "$change_state_file"

fetch_img $current

rm $change_state_file
touch $change_state_file