#!/usr/bin/python

# usage: (echo "any' or '1'='1"; echo "any' or '1'='1") | nc ctf-server port

import socket
import sys
import subprocess
import thread


def on_new_client(clientsocket, addr):

    print '[DEBUG]: on_new_client()'
    try:
        proc = subprocess.Popen(query_py, shell=True, stdout=clientsocket, stderr=subprocess.PIPE, \
                                                    stdin=clientsocket)
        clientsocket.close()
    
    except Exception as err:
        print '[ERROR]: ', err
        clientsocket.close()

# main
if __name__ == "__main__":

    query_py = 'python -u /home/ctf/Challenges/HTTP_Server/query.py'
    if len(sys.argv) == 2:
        port = int(sys.argv[1])
    else:
        port = 36002
    host = '' # any host can connect

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(30) # how many users ?

    print "Listen on port: ", port
    print 'Exit with Ctrl+C\n'

    while True:

        try:
            conn, addr = s.accept()
            print '[DEBUG]: Connection address: ', addr
            thread.start_new_thread(on_new_client, (conn, addr))

        except Exception as err:
            print '[ERROR]: ', err
        except KeyboardInterrupt:
            s.close()
            print 'Exit Script'
            sys.exit(0)

# EOF
