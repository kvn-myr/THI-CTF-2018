#! /usr/bin/env python3
##

import sys
import hashlib

res = ""
for line in sys.stdin.readlines():
    line = line[:-1]
    h = hashlib.sha1()
    h.update(line.encode())
    h_temp = h.hexdigest()
    val_temp = []
    for c in h_temp:
        val_temp.append(c)
    val = []
    val.append(val_temp[10])
    val.append(val_temp[14])
    val.append(val_temp[3])
    val.append(val_temp[22])
    val.append(val_temp[32])
    val.append(val_temp[35])
    val.append(val_temp[15])
    val.append(val_temp[27])
    val.append(val_temp[12])
    val = ''.join(val)
    temp = []
    for c in line:
        temp.append(c)
    if len(temp) == 32 and val == "773abe1f5":
        temp2 = []
        temp2.append(temp[14])
        temp2.append(temp[15])
        temp2.append(temp[16])
        temp2.append(temp[19])
        temp2.append(temp[20])
        temp2.append(temp[21])
        temp2.append(temp[4])
        temp2.append(temp[6])
        temp2.append(temp[8])
        temp2 = ''.join(temp2)
        res = temp2
    if res != "" and res != "1":
        print("Congratulations! You found a flag: THICTF{" + res + "}")
        res = "1"
if res == "":
    print("You have not found a flag!")
