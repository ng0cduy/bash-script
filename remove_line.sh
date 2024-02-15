#!/bin/bash -euox
echo "Reading data from a file:"
while read -r line; do
    touch "temp_remove_line.txt"
    echo "$line"
    test=$(find phase  -type f -name "*.txt" -exec grep "$line" {} +)
    echo "$test" >> "temp_remove_line.txt"
done < "remove_line.txt"

while read -r line; do
    echo "$line"
done < "temp_remove_line.txt"