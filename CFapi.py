# Rick Mur - Maverick.Solutions - (c) 2016
__author__ = "Rick Mur"
__version__ = "1.0"

from CFupdater import updateCF
from bottle import route, run, request, abort
from pprint import pprint as pp
from base64 import b64decode

@route("/update")
def test():

    authHeader = request.headers.get("Authorization").split(" ")
    auth = b64decode(authHeader[1]).split(":",1)
    username = auth[0]
    password = auth[1]
    hostname = request.query.hostname
    myip = request.query.myip

    print ("Username: " + username)
    print ("Password: " + password)
    print ("Hostname: " + hostname)
    print ("New IP: " + myip)

run(host='0.0.0.0', port=80, debug=True)

