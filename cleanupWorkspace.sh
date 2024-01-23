#!/bin/bash

echo "Reading data from a file:"
while read line; do
  file_path=$(grep -r "$line" "phase/PHASE-IMG" | cut -d ":" -f1)
  file_path1=$(echo $file_path | cut -d '/' -f1)
  file_path2=$(echo $file_path | cut -d '/' -f2)
  file_path3=$(echo $file_path | cut -d '/' -f3)
  file_path4=$(echo $file_path | cut -d '/' -f4)
  echo "$file_path is with ID: $line"
  deleted_path="$file_path1/$file_path2/$file_path3/$file_path4"
  echo "$deleted_path"
  echo "deleting $deleted_path"
  if [[ $deleted_path == "///" ]]
  then
    echo "Error"
  else
    rm -rf "$deleted_path"
  fi
done < "del_list.txt"