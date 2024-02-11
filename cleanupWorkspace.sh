#!/bin/bash

echo "Reading data from a file:"
while read line; do
  line1=$(echo "$line" | rev | cut -d "/" -f1 | rev)
  file_path=$(grep -r "$line1" "phase/PHASE-IMG" | cut -d ":" -f1)
  file_path1=$(echo $file_path | cut -d '/' -f1)
  file_path2=$(echo $file_path | cut -d '/' -f2)
  file_path3=$(echo $file_path | cut -d '/' -f3)
  file_path4=$(echo $file_path | cut -d '/' -f4)
  if [[ -z $file_path ]]
  then
    echo "Folder containes ID $line1 not exist"
  else
    deleted_path="$file_path1/$file_path2/$file_path3/$file_path4"
    echo "$file_path is with ID: $line1"
    echo "$deleted_path"
    echo "deleting $deleted_path"
    rm -rf "$deleted_path"
  fi


#   if [[ $deleted_path == "///" ]]
#   then
#     echo "Error"
#   else

#   fi
done < "del_list.txt"