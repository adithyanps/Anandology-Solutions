import sys
import socket
import urllib
def myip(x):
 print "LOCAL HOST=%s"% (urllib.localhost())
 print "IP=%s"% (socket.gethostbyname(x))
myip(sys.argv[1])
