#!/bin/bash
string_data=$1

a=$(echo "$string_data" | sed 's/.\{3\}/& /g' | xargs)
echo "hotwheels tts "$a