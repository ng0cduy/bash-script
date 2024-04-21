#!/usr/bin/bash -x
source function.sh
set -e

python3 fetch_info_link.py

input_path=$1
input_dir="phase/phase$input_path"
if [ -d $input_dir ]
then
    echo "$input_dir exist"
else
    echo "$input_dir not exist"
    mkdir -p "$input_dir"
    touch "$input_dir/phase$input_path.txt"
fi
cat "fetch_info_link_output.txt" >> "$input_dir/phase$input_path.txt"
fetch_img "$input_path"
rm "fetch_info_link_input.txt" "fetch_info_link_output.txt"
touch "fetch_info_link_input.txt" "fetch_info_link_output.txt"
