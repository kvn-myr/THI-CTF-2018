from flask import Flask, request
import cgi, subprocess, os, binascii, re
app = Flask(__name__)

# Import Flag
flag = open('flag.txt').readline()


# Check for XSS
def check_xss(page,flag):
    proc = subprocess.Popen(["timeout","5","phantomjs", "check.js"], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
    if not os.path.isdir("./pages"):
        os.mkdir("./pages")
    f = "pages/" + binascii.b2a_hex(os.urandom(8)).decode() + '.html'
    url = 'http://localhost:5000/' + f
    try:
        fo = open(f, "w")
        fo.write(page)
        fo.close()
        proc.stdin.write(f.encode())
        proc.stdin.close()
        result = proc.stdout.readline().strip()
        result = result.decode()
    except:
        pass
    finally:
        os.remove(f)
    if result == 'THI':
        data = '<br>Challenge done! Here is your flag: %s' % flag
    elif result:
        data = "<br>Please trigger an alert with 'THI' instead of %s!" % (cgi.escape(result))
    else:
        data = "<br>The web application seems to work normally. But don't forget, this challenge isn't as easy as the first time, is it? Next try..."
    return data


# Webserver
@app.route("/")
def index():
    return """<html><body>
            <h1>THI-CTF</h1>
            <h2>WEB-Challenge</h2>
            Hey here is an other WEB challenge. Start challenge
            <a href="challenge?name=Hacker">here</a>
            </body></html>"""



@app.route("/challenge")
def challenge():
    msg = request.args.get('name','')
    # Filter for < followed by literal
    msg = re.sub(r"""<[a-z/]""", "", msg, flags=re.IGNORECASE)
    # Filter for "THI" or 'THI'
    msg = re.sub(r"""["']THI["']""", "", msg, flags=re.IGNORECASE)
    data = "Welcome back %s!" % msg
    data += check_xss(data,flag)
    return data



if __name__ == "__main__":
    app.run()
