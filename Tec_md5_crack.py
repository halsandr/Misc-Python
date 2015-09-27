import hashlib, os, time, math
from hashlib import md5
from getpass import getpass

def screen_clear():
	if os.name == 'nt':
		return os.system('cls')
	else:
		return os.system('clear')

screen_clear()

print ""
print "Welcome to the Technicolor md5 cracker"
print ""

user = raw_input("Username: ")
print ""
nonce = raw_input("Nonce: ")
print ""
hash = raw_input("Hash: ")
print ""
file = raw_input("Wordlist: ")
print ""

realm = "Technicolor Gateway"
qop = "auth"
uri = "/login.lp"

HA2 = md5("GET" + ":" + uri).hexdigest()

wordlist = open(file, 'r')

time1 = time.time()

tested = 0

for word in wordlist:
	pwd = word.replace("\n","") 
	HA1 = md5(user + ":" + realm + ":" + pwd).hexdigest()
	hidepw = md5(HA1 + ":" + nonce +":" + "00000001" + ":" + "xyz" + ":" + qop + ":" + HA2).hexdigest()
	tested += 1
	if hidepw == hash:
		screen_clear()
		time2 = time.time()
		timetotal = math.ceil(time2 - time1)
		print pwd + " = " + hidepw + " (in " + str(timetotal) + " seconds)"
		print ""
		end = raw_input("hit enter to exit")
		exit()
	if tested % 100000 == 0:
		screen_clear()
		print str(tested) + " passwords tested."
		
wordlist.close()

screen_clear()
time2 = time.time()
totaltime = math.ceil(time2 - time1)
print "Sorry, out of " + str(tested) + " passwords tested, your password was not found (in " + str(totaltime) + " seconds)"
print ""
end = raw_input("hit enter to exit")
screen_clear()
exit()
