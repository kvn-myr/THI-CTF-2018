# HTTP_Server

**Description of the Challenge:**
I think there is something hidden on this server... But I don't know how to access it.

## Setup
To start the server:
```$ python start_threaded_server.py [port] admin:ctf_l3t_me_iN```

Server now runs on `localhost:port`. First is the sql-injection part of the challenge:

```$ nc [host] [port] (query.py)```

Once the login is known from the sql injection attack, the challenge can be continued.

## Solution
The participant, let's call him Harry, has to find the key inside the 424 files that he can download after logging into the server. For the Login Harry has to do a SQL Injection. For that he will use the provided script *query.py* and do a SQL-Injection attack as shown in A) under Commands & Scripts. With the correct login, he can continue to downloading files from the server. Those 424 files are stored on the server and can be retrieved by issuing a POST cmd to (SERVER)/files with the parameter *file_number*. Harry could manually download files 1 to 424 through the web page on localhost, which would however take eons, so he has to use curl or a similar tool to automate downloading files 1 to 424. See B) in Commands & Scripts. Now he has all 424 files which all have 37 byte. 423 files have 37 random bytes, 1 file has 37 bytes which is the base64 encoded flag. How will Harry find the right file? By using grep and his intuition that the flag will be base64 encoded. See C) in Commands & Scripts Last, he has to encode that Base64 encoded flag.

------------------ Commands & Scripts ------------------

---------------- A)
```
$ nc 10.84.56.56 36002 // ip-adresse/port vom server muss angepasst werden 
Input username: any' or '1=1
Input password: any' or '1=1
```
---------------- B)
```
#!/bin/bash
for((i=$1; i<=$2; i++)); do
  $(curl -d "file_number=$i" -u "admin:ctf_l3t_me_iN" -o "file_$i" "localhost:8080/files") || continue
done
```
Usage: `$ cd ~/Downloads && sudo bash downloader.sh 1 424`

Notes:
* This *downloader.sh* file comes with the git pull but not with with the CTFd
* It won't be "localhost" for Harry but the IP address of our server. He might also not use curl at all and something else like wget. 
* He also won't know its exactly 424 files, so his script might download some non-existant files which will result in files with a 404 error message inside. 

---------------- C)
```grep "=" file_*```

Usage: `$ (as shown)`

Notes:
* This will show that one file which has the base64 encoded flag inside (base64 has a "=" at the end).

## Flag
THICTF{oh_no_you_found_me}
