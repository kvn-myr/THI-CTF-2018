#! /usr/bin/env python3
##

import hashlib

text_file = open("./md5.txt", "r")
for line in text_file:
    line = line[:-1]
    hash_file = hashlib.md5()
    hash_file.update(line.encode())
    print(hash_file.hexdigest())
