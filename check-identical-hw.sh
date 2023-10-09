#!/bin/bash
HW_file="hw.txt"
OS=$(uname -m)
if [ "$OS" = "x86_64" ]
then
    HW_layered_folder="$Desktop/newHW_layered"
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
        fi
done < "$HW_file"
rm -rf "temp_list.txt"