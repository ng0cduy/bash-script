#!/bin/bash
rm -f "temp.txt"
rm -f "a.html"
input_link=$1
curl -s --output "a.html" "$input_link"
links=$(cat "a.html" | grep -Eo https://auctions.c.yimg.jp/images.auctions.yahoo.co.jp/image/dr000/auc[0-9]{4}/users/[A-Za-z0-9]*/i-img[A-Za-z0-9-]*.jpg| sort -u)
echo "$links" > temp.txt

while IFS= read -r links_img
do
    echo "$links_img"
done < "temp.txt"

rm -f "temp.txt"
rm -f "a.html"