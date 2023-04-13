#!/bin/bash -ex

RED='\033[0;31m'
NC='\033[0m' # No Color
BLUE='\033[0;34m'         # Blue
PURPLE='\033[0;35m'       # Purple
CYAN='\033[0;36m'         # Cyan
WHITE='\033[0;37m'        # White

# Bold
BBlack='\033[1;30m'       # Black
BRed='\033[1;31m'         # Red
BGreen='\033[1;32m'       # Green
BYellow='\033[1;33m'      # Yellow
BBlue='\033[1;34m'        # Blue
BPurple='\033[1;35m'      # Purple
BCyan='\033[1;36m'        # Cyan
BWhite='\033[1;37m'       # White

input=$1
output="/mnt/c/Users/bduy1/Desktop/$2"
mkdir -p "$output"
while IFS= read -r line
do
    link=$(echo "$line" | cut -d ',' -f 1)
    name=$(echo "$line" | cut -d ',' -f 2)
    curl "$link" --output "$output/$name.jpg"
done < "$input"