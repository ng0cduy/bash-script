#!/bin/bash -x
set -e
source function.sh
echo "Reading data from a file:"
from=$1
to=$2
while read line; do
  line0=$(echo "$line" | cut -d "," -f1)
  line1=$(echo "$line0" | rev | cut -d "/" -f1 | rev)
  file_path=$(grep -r "$line1" "phase/PHASE-IMG/phase$from-img" | cut -d ":" -f1)
  file_path1=$(echo "$file_path" | cut -d '/' -f1)
  file_path2=$(echo "$file_path" | cut -d '/' -f2)
  file_path3=$(echo "$file_path" | cut -d '/' -f3)
  file_path4=$(echo "$file_path" | cut -d '/' -f4)
  if [[ -z $file_path ]]
  then
    echo "Folder containes ID $line1 not exist"
  else
    move_path="$file_path1/$file_path2/$file_path3/$file_path4"
    echo "$move_path is with ID: $line1"
    new_path="$file_path1/$file_path2/phase$to-img/$file_path4"
    to_phase="$file_path1/$file_path2/phase$to-img"
    if [ ! -d "$to_phase" ];
    then
        echo "$to_phase not exist, create a new folder"
        mkdir -p "$to_phase"
        mkdir -p "phase/phaseInfo/phase$to"
        cp "phase/phaseInfo/phase$from/phase$from""_remain.txt" "phase/phaseInfo/phase$to/phase$to.txt"
        cp "phase/phaseInfo/phase$from/phase$from""_remain.txt" "phase/phaseInfo/phase$to/phase$to""_copy.txt"
        cp "phase/phaseInfo/phase$from/phase$from""_remain.txt" "phase/phaseInfo/phase$to/phase$to""_remain.txt"
    fi
    mv "$move_path" "$new_path"
    echo "Moved $move_path to $new_path"
  fi
# fetch_img "$to"
done < "moveItems.txt"
deleted_line_file_orig="phase/phaseInfo/phase$from/phase$from.txt"
deleted_line_file_copy="phase/phaseInfo/phase$from/phase$from""_copy.txt"
echo $delted_line_file_copy
while read line; do
    line0=$(echo "$line" | cut -d "," -f1)
    line1=$(echo "$line0" | rev | cut -d "/" -f1 | rev)
    echo $line1
    replace_line_number=$(cat $deleted_line_file_orig | grep -n $line1 | cut -d: -f1)
    echo $replace_line_number
    if [ -n $replace_line_number ]
    then
        sed -i "$replace_line_number d" $deleted_line_file_orig
        sed -i "$replace_line_number d" $deleted_line_file_copy
    fi
done < "moveItems.txt"

rm -rf "moveItems.txt"
touch "moveItems.txt"