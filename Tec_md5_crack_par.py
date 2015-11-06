#!/usr/bin/env python

import hashlib, os, time, math
from hashlib import md5
from multiprocessing import Pool, cpu_count

def screen_clear(): # Small function for clearing the screen on Unix or Windows
	if os.name == 'nt':
		return os.system('cls')
	else:
		return os.system('clear')

cores = cpu_count() # Var containing number of cores (Threads)

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

time1 = time.time() # Begins the 'Clock' for timing

realm = "Technicolor Gateway" # These 3 variables dont appear to change
qop = "auth"
uri = "/login.lp"

HA2 = md5("GET" + ":" + uri).hexdigest() # This hash doesn't contain any changing variables so doesn't need to be recalculated

file = open(file, 'r') # Opens the wordlist file
wordlist = file.readlines() # This enables us to use len()

break_points = []  # List that will have start and stopping points
for i in range(cores):  # Creates start and stopping points based on length of word list
    break_points.append({"start":int(math.ceil(len(wordlist)/cores * i)), "stop":int(math.ceil(len(wordlist)/cores * (i + 1)))})


def pwd_find(start, stop):
    for number in range(start, stop):
		word = (wordlist[number])
		pwd = word.replace("\n","")
		HA1 = md5(user + ":" + realm + ":" + pwd).hexdigest()
		hidepw = md5(HA1 + ":" + nonce +":" + "00000001" + ":" + "xyz" + ":" + qop + ":" + HA2).hexdigest()
		if hidepw == hash:
			screen_clear()
			time2 = time.time() # stops the 'Clock'
			timetotal = math.ceil(time2 - time1) # Calculates the time taken
			print pwd + " = " + hidepw + " (in " + str(timetotal) + " seconds)"
			print ""
			p.terminate() # 
			p.join()
			file.close()
			end = raw_input("hit enter to exit")
			exit()

if __name__ == '__main__':  # Added this because the multiprocessor module acts funny without it.

    p = Pool(cores)  # Number of processors to utilize.
    for i in break_points:  # Cycles though the breakpoints list created above.
        a = p.apply_async(pwd_find, kwds=i, args=tuple())  # This will start the separate processes.
    p.close()
    p.join()

file.close()

screen_clear()
time2 = time.time() # Stops the 'Clock'
totaltime = math.ceil(time2 - time1) # Calculates the time taken
print "Sorry your password was not found (in " + str(totaltime) + " seconds)"
print ""
end = raw_input("hit enter to exit")
screen_clear()
exit()
