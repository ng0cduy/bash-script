#!/bin/bash
HW_file="hw.txt"
HW_layered_folder="$HOME/Desktop/newHW_layered"
ls "$HW_layered_folder" > "temp_list.txt"
echo "*************************"
while read line;
    do
        if grep -q "$line" "temp_list.txt";
        then
            echo "$line"
        fi
done < "$HW_file"
rm -rf "temp_list.txt"