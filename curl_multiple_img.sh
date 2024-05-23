#!/bin/bash -x
set -e
# Check if the URL file is provided
# if [ -z "$1" ]; then
#     echo "Usage: $0 url_file"
#     exit 1
# fi
input_folder=$1
input_file="curl_multiple_img.txt"
# Read the file line by line
while IFS= read -r url; do
    # Use curl to fetch the content
    curl -O "$input_folder/$url"
done < "$input_file"
