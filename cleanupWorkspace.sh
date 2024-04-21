#!/bin/bash
set -e
source function.sh
echo "Reading data from a file:"
while read line; do
  line1=$(echo "$line" | rev | cut -d "/" -f1 | rev)
  file_path=$(grep -r "$line1" "phase/PHASE-IMG" | cut -d ":" -f1)
  file_path1=$(echo $file_path | cut -d '/' -f1)
  file_path2=$(echo $file_path | cut -d '/' -f2)
  file_path3=$(echo $file_path | cut -d '/' -f3)
  phase_num=$(echo $file_path3 | cut -d '-' -f1)
  file_path4=$(echo $file_path | cut -d '/' -f4)
  if [[ -z $file_path ]]
  then
    echo "Folder containes ID $line1 not exist"
  else
    deleted_path="$file_path1/$file_path2/$file_path3/$file_path4"
    delete_file_path="phase/$phase_num/$phase_num"
    replace_line_number=$(cat "$delete_file_path.txt" | grep -n $line1 | cut -d: -f1)
    # if [ -n $replace_line_number ]
    # then
    #     sed -i "$replace_line_number d" "$delete_file_path.txt"
    #     sed -i "$replace_line_number d" "$delete_file_path""_copy.txt"
    #     echo "Delete line with pattern $line1 in $delete_file_path.txt and $delete_file_path""_copy.txt"
    # fi
    echo "$file_path is with ID: $line1"
    echo "$deleted_path"
    echo "deleting $deleted_path"
    rm -rf "$deleted_path"
  fi
done < "cleanupWorkspace.txt"

rm "cleanupWorkspace.txt"
touch "cleanupWorkspace.txt"