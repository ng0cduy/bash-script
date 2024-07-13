#!/bin/bash -x
set -e
# Check if the URL file is provided
# if [ -z "$1" ]; then
#     echo "Usage: $0 url_file"
#     exit 1
# fi
input_folder=$1
input_file="curl_multiple_img.txt"
number=0
increment=1
mkdir "$input_folder"
# Read the file line by line
while IFS= read -r url; do
    filename="$number.jpg"
    # Use curl to fetch the content
    curl --output "$input_folder/$filename" "$url"
    number=$((number + increment))
done < "$input_file"
