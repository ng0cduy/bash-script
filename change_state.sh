#!/bin/bash
set -e
change_state_file="change_state_list.txt"
current=$1
current_file="phase/phase$current/phase$current.txt"
# search_link="https://jp.mercari.com/item/m28255989835"
# replace_line_number=$(cat $in | grep -n $search_link | cut -d: -f1)
# sed -i "$replace_line_number s/NA/JP/" $in



while IFS= read -r line
do
    replace_line_number=$(cat $current_file | grep -n $line | cut -d: -f1)
    sed -i "$replace_line_number s/,NA,/,JP,/" $current_file
    sed -n "$replace_line_number p" $current_file
done < "$change_state_file"

export fetch_mer_script="/mnt/d/project/bash-script/fetch_img_by_list.sh"
export bash_scipt_repo="/mnt/d/project/bash-script"
fetch_img()
{
    bash -x "$fetch_mer_script" "$bash_scipt_repo/phase/phase$1/phase$1.txt" /mnt/d/project/bash-script/phase/PHASE-IMG
}

fetch_img $current

rm $change_state_file
touch $change_state_file