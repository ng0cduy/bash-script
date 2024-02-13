#!/bin/bash -euox
echo "Reading data from a file:"
from=$1
to=$2
while read line; do
  line1=$(echo "$line" | rev | cut -d "/" -f1 | rev)
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
    fi
    mv "$move_path" "$new_path"
    echo "Moved $move_path to $new_path"
  fi
done < "move_list.txt"