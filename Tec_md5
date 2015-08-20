import hashlib, os
from hashlib import md5
from getpass import getpass

def screen_clear():
	if os.name == 'nt':
		return os.system('cls')
	else:
		return os.system('clear')

screen_clear()

print ""
print "Welcome to the Technicolor md5 generator"
print ""

user = raw_input("Username: ")
print ""
pwd = getpass()
print ""
nonce = raw_input("Nonce: ")

realm = "Technicolor Gateway"
qop = "auth"
uri = "/login.lp"

HA1 = md5(user + ":" + realm + ":" + pwd).hexdigest()

HA2 = md5("GET" + ":" + uri).hexdigest()

hidepw = md5(HA1 + ":" + nonce +":" + "00000001" + ":" + "xyz" + ":" + qop + ":" + HA2).hexdigest()

print ""
print "Your 'hidepw' value is: " + hidepw

print ""
end = raw_input("hit enter to exit")
screen_clear()
exit()
