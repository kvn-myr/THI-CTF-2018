#!/bin/bash

#THICTF{oh_no_you_found_me}
flagAsBase64="VEhJQ1RGe29oX25vX3lvdV9mb3VuZF9tZX0=" #36 letters

for((i=$1; i<=$2; i++)); do
  if [ "$i" = "$3" ]; then
    echo "$flagAsBase64" > "file_$i";
  else  
    echo $(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 36 | head -n 1) > "file_$i";
  fi
done
