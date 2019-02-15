import BaseHTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler
import sys
import base64
from os import curdir, sep
import cgi

key = ""

class AuthHandler(SimpleHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_AUTHHEAD(self):
        self.send_response(401)
        self.send_header('WWW-Authenticate', 'Basic realm=\"\"')
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        global key
        if self.headers.getheader('Authorization') == None:
            self.do_AUTHHEAD()
            self.wfile.write('No auth header received')
            pass
        elif self.headers.getheader('Authorization') == 'Basic '+key:
            SimpleHTTPRequestHandler.do_GET(self)
            pass
        else:
            self.do_AUTHHEAD()
            #self.wfile.write(self.headers.getheader('Authorization'))
            self.wfile.write('Authentication failed')
            pass

    def do_POST(self):
        if self.path=="/files":
			form = cgi.FieldStorage(
				fp=self.rfile, 
				headers=self.headers,
				environ={'REQUEST_METHOD':'POST',
		                 'CONTENT_TYPE':self.headers['Content-Type'],
			})

        file_number = form["file_number"].value;
        try:
            with open("./files/file_%s" % file_number, 'rb') as file:
                self.send_response(200)
                self.send_header('Content-Disposition', 'attachment; filename="file_%s"' % file_number)
                self.send_header('Content-type','application/octet-stream')
                self.end_headers()
                self.wfile.write(file.read())
            return
        except IOError as e:
            self.send_error(404,'File Not Found: %s' % e)

def run(HandlerClass = AuthHandler,
         ServerClass = BaseHTTPServer.HTTPServer):
    BaseHTTPServer.test(HandlerClass, ServerClass)


if __name__ == '__main__':
    try:
        if len(sys.argv)<3:
            print "Usage: start_server.py [port] [username:password]"
            sys.exit()
        key = base64.b64encode(sys.argv[2])
        run()
    except KeyboardInterrupt:
	    print 'Shutting down server'
