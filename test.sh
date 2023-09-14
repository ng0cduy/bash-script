#!/bin/bash -x
set -e
start="https://s1.cdn.autoevolution.com/images/news/gallery/"
mid=$1
end=".jpg"
file_prefix=$2
folder_storage=$3
OS=$(uname -m)
rm -rf "$folder_storage"
cur_pwd=$(pwd)
mkdir "$cur_pwd/$folder_storage"
for i in {1..100}
do
    filename_url="$start""$mid""$i""$end"
    output_filename="$cur_pwd/$2/$file_prefix""_$i""$end"
    curl "$filename_url" --output "$output_filename"
    if [ "$OS" = "x86_64" ]
    then
        file_size=$(du -kh "$output_filename" | grep -Eo '[0-9]{1,4}' | head -1)
    elif [ "$OS" = "arm64" ]
    then
        file_size=$(du -kh "$output_filename" | grep -Eo '[0-9]+K' | grep -Eo '[0-9]+')
    fi
    if [ "$file_size" == 0 ] || cat "$output_filename" | grep "404 Not Found"
    then
        rm -rf "$output_filename"
        break
    fi
done
