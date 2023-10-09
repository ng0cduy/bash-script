#!/bin/bash
HW_file="hw.txt"
OS=$(uname -m)
if [ "$OS" = "x86_64" ]
then
    HW_layered_folder="$desktop/case-HW/img-storage"
elif [ "$OS" = "arm64" ]
then
    HW_layered_folder="$HOME/Desktop/newHW_layered"
fi
ls "$HW_layered_folder" > "temp_list.txt"
while read line;
    do
        if grep -q "$line" "temp_list.txt";
        then
            echo "$line"
            echo "$line" >> "count_line.txt"
        fi
done < "$HW_file"
cat "count_line.txt" | wc -l
rm -rf "temp_list.txt" "count_line.txt"