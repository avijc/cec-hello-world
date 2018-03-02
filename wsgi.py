import socket
import datetime
from flask import Flask

application = Flask(__name__)

@application.route("/")
def hello():
    logfile = "/mnt/storedbits/logfile.txt"
    myname = socket.gethostname()
    timestamp = str(datetime.datetime.now())
    writelog(logfile, myname, timestamp)
    return """<!DOCTYPE html><html><head><title>Silver Lining</title></head>
<body>
<h1>Hi visitor!</h1>
This magnificent Silver Lining webpage was brought to you by """ + myname + " at " + timestamp + """.<br>
Here is a log of past visits:<br>
""" + getlog(logfile) + "\n</body></html>"

def writelog(filename, myname, timestamp):
    try:
        log = open(filename, "a")
        log.write(myname + " " + timestamp + "\n")
        log.close()
    except IOError:
        return "I'm really sorry for the inconvenience, but the log file could not be opened for appending :-/"

def getlog(filename):
    try:
        log = open(filename, "r")
        retval = "<pre>\n" + log.read() + "</pre>"
        log.close()
        return retval
    except IOError:
        return "I'm really sorry for the inconvenience, but the log file could not be opened for reading :-/"

if __name__ == "__main__":
    application.run()
