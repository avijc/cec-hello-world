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
    return "Hi visitor! This magnificent Silver Lining webpage was brought to you by " + myname + " at " + \
        timestamp + ". Here is a log of past visits:<br><br>\n" + getlog(logfile)

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
        retval = "<pre>" + log.read() + "</pre>"
        log.close()
        return retval
    except IOError:
        return "I'm really sorry for the inconvenience, but the log file could not be opened for reading :-/"

if __name__ == "__main__":
    application.run()
