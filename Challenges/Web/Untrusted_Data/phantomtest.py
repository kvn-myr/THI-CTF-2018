#! /usr/bin/env python

import subprocess, os

msg = "<script>alert('5321')</script>"

# Open phantomjs
proc = subprocess.Popen(["timeout","5","phantomjs", "check.js"], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
f = "./temp.html"
try:
    fo = open(f, "w")
    fo.write(msg)
    fo.close()
    proc.stdin.write(f.encode())
    proc.stdin.close()
    res = proc.stdout.readline().strip()
    res = res.decode()
except:
    pass
finally:
    os.remove(f)

if("5321" == res):
    print("phantomjs: OK")
else:
    print("phantomjs: ERROR")
