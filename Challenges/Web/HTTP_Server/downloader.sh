#!/bin/bash
for((i=$1; i<=$2; i++)); do
  $(curl -d "file_number=$i" -u "admin:ctf_l3t_me_iN" -o "file_$i" "localhost:8080/files") || continue
done
