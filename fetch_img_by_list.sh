#!/bin/bash -x
set -e
# ./fetch_img_by_list.sh phase/phase3/phase3.txt ~/Desktop/IMG-FOLDER 2>&1 | tee log.log
# ./fetch_img_by_list.sh phase1.txt /mnt/c/Users/bduy1/Desktop 2>&1 | tee log.log
# https://paypayfleamarket.yahoo.co.jp/item/z225582006
export RED='\033[0;31m'
export NC='\033[0m' # No Color
export BLUE='\033[0;34m'         # Blue
export PURPLE='\033[0;35m'       # Purple
export CYAN='\033[0;36m'         # Cyan
export WHITE='\033[0;37m'        # White

# Bold
export BBlack='\033[1;30m'       # Black
export BRed='\033[1;31m'         # Red
export BGreen='\033[1;32m'       # Green
export BYellow='\033[1;33m'      # Yellow
export BBlue='\033[1;34m'        # Blue
export BPurple='\033[1;35m'      # Purple
export BCyan='\033[1;36m'        # Cyan
export BWhite='\033[1;37m'       # White
DEFAUL_DOWNLOAD_IMG="https://static.mercdn.net/item/detail/orig/photos"
OS=$(uname -m)

_name_="list_hang"
input=$1
input_base_name=$(basename "$input" .txt)
input_dir_name=$(dirname "$input")
destination_folder="$2/$input_base_name""-img"
rm -rf "$input_dir_name/$input_base_name""_copy.txt"
rm -rf "$input_dir_name/$input_base_name""_remain.txt"
cp "$input" "$input_dir_name/$input_base_name""_copy.txt"
bought_list_without_link="$destination_folder/$_name_.txt"
#create summary bought file
rm -rf "$bought_list_without_link"
rm -rf "$input_base_name""_remain.txt"
# touch "$bought_list_without_link"
touch "$input_dir_name/$input_base_name""_remain.txt"
# create images folder
mkdir -p "$destination_folder"
touch "$bought_list_without_link"
while IFS= read -r line
do
    link=$(echo "$line" | cut -d ',' -f 1)
    name=$(echo "$line" | cut -d ',' -f 2)
    ID=$(echo "$link" | rev | cut -d'/' -f 1 | rev)
    state=$(echo "$line" | cut -d ',' -f 3)
    condition=$(echo "$line" | cut -d ',' -f 4)
    user_url=$(echo "$line" | cut -d ',' -f 5)
    #parse bought link and remain link(not available yet)
    if [ "$state" = "JP" ] || [ "$state" = "JP-VN" ]
    then
        echo "$name,$condition" >> "$bought_list_without_link"

    elif [ "$state" = "NA" ]
    then
        echo "$link,$name,$state,$condition" >> "$input_dir_name/$input_base_name""_remain.txt"
    fi
    # spawn folder with name
    product_folder="$destination_folder/$name"
    product_folder_1="$destination_folder/[VN]_$name""_[$condition]"
    #check if secret file already exsist or not by checking name and ID, if not
    # create the secret file and curl img
    # spawn a secret file into link, pass name and ID into link
    # else do nothing
    if [ -d "$product_folder" ]
    then
        secret_ID=$(cat "$product_folder/secret_link")
        chmod 444 "$product_folder/secret_link"
        if [ "$secret_ID" = "$ID" ]
        then
            echo -e "${RED}Folder ${product_folder} Already exist ${NC}"
        fi
    elif [ -d "$product_folder_1" ]
    then
        secret_ID=$(cat "$product_folder_1/secret_link")
        chmod 444 "$product_folder_1/secret_link"
        if [ "$secret_ID" = "$ID" ]
        then
            echo -e "${CYAN}Folder ${product_folder_1} Already exist and already changed the name ${NC}"
        fi
    else
        mkdir "$product_folder"
        touch "$product_folder/secret_link"
        echo "$ID" >> "$product_folder/secret_link"
        echo "$user_url" >> "$product_folder/secret_link"
        chmod 444 "$product_folder/secret_link"
        if [[ "$link" == *"jp.mercari.com/item"* ]] || [[ "$link" == *"jp.mercari.com/en/item"* ]];
        then
            for i in {1..20}
            do
                filename="$name""_$i.jpg"
                product_img="$product_folder/$filename"
                download_link="$DEFAUL_DOWNLOAD_IMG/$ID""_$i.jpg"
                curl "$download_link" --output "$product_img"
                if [ "$OS" = "x86_64" ]
                then
                    file_size=$(du -kh "$product_img" | grep -Eo '[0-9]{1,4}' | head -1)
                elif [ "$OS" = "arm64" ]
                then
                    file_size=$(du -kh "$product_img" | grep -Eo '[0-9]+K' | grep -Eo '[0-9]+')
                fi
                if [ "$file_size" == 0 ]
                then
                    rm -rf "$product_img"
                    break
                fi
            done
        elif [[ "$link" == *"paypayfleamarket.yahoo.co.jp/item"* ]];
        then
            curl -s --output "a.html" "$link"
            links=$(cat "a.html" | grep -Eo "https://auctions.c.yimg.jp/images.auctions.yahoo.co.jp/image/dr000/auc[0-9]{4}/users/[A-Za-z0-9]*/i-img[A-Za-z0-9-]*.jpg"| sort -u)
            echo "$links" > temp.txt
            i=1
            while IFS= read -r line
            do
                filename="$name""_$i.jpg"
                product_img="$product_folder/$filename"
                curl "$line" --output "$product_img"
                i=$((i+1))
            done < "temp.txt"
            rm -f "temp.txt"
            rm -f "a.html"
        elif [[ "$link" == *"shops/product"* ]];
        then
            python3 fetch_mer_shop_img_list.py "$link"
            i=1
            while IFS= read -r line
            do
                filename="$name""_$i.jpg"
                product_img="$product_folder/$filename"
                curl "$line" --output "$product_img"
                i=$((i+1))
            done < "a.txt"
            rm -f "a.txt"
        fi
    fi
done < "$input"

while IFS= read -r line
do
    bought_name=$(echo "$line" | cut -d ',' -f 1)
    bought_state=$(echo "$line" | cut -d ',' -f 2)
    file=$(ls "$destination_folder" | grep "$bought_name")
    file1="[VN]_$bought_name""_[$bought_state]"

    if [ -z "$file" ]
    then
        echo -e "${RED}Folder ${destination_folder}/${bought_name} not found or not a folder ${NC}"
    elif [ "$file" = "$file1" ]
    then
        echo -e "${CYAN}Folder ${destination_folder}/${file1} already changed the name and state${NC}"
    else
        mv "$destination_folder/$bought_name" "$destination_folder/[VN]_$bought_name""_[$bought_state]"
    fi
done < "$bought_list_without_link"

total_product_list=$(cat "$bought_list_without_link"| sed '/^\s*$/d'| wc -l)
{
    echo "---------------------------------------------"
    echo "Tổng đơn: $total_product_list"
    echo "---------------------------------------------"
} >> "$bought_list_without_link"
