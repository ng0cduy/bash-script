#!/usr/bin/bash -x
set -e

python3 fetch_img_by_list.py

export fetch_mer_script="/mnt/d/project/bash-script/fetch_img_by_list.sh"
export bash_scipt_repo="/mnt/d/project/bash-script"
fetch_img()
{
    bash -x "$fetch_mer_script" "$bash_scipt_repo/phase/phase$1/phase$1.txt" /mnt/d/project/bash-script/phase/PHASE-IMG
}

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
cat "output.txt" >> "$input_dir/phase$input_path.txt"
fetch_img "$input_path"
echo > "input.txt"
echo > "output.txt"