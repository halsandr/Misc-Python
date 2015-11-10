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
screen_clear()
print "Cracking the password for \"" + user + "\" using " 
time1 = time.time() # Begins the 'Clock' for timing

realm = "Technicolor Gateway" # These 3 variables dont appear to change
qop = "auth"
uri = "/login.lp"

HA2 = md5("GET" + ":" + uri).hexdigest() # This hash doesn't contain any changing variables so doesn't need to be recalculated

file = open(file, 'r') # Opens the wordlist file
wordlist = file.readlines() # This enables us to use len()
length = len(wordlist)

screen_clear()
print "Cracking the password for \"" + user + "\" using " + str(length) + " words"

break_points = []  # List that will have start and stopping points
for i in range(cores):  # Creates start and stopping points based on length of word list
    break_points.append({"start":int(math.ceil((length+0.0)/cores * i)), "stop":int(math.ceil((length+0.0)/cores * (i + 1)))})

solved = False

def solver(state):
	if state == True:
		p.terminate
		p.join
		global solved
		solved = state

def pwd_find(start, stop):
    for number in range(start, stop):
		word = (wordlist[number])
		pwd = word.replace("\n","") # Removes newline character
		HA1 = md5(user + ":" + realm + ":" + pwd).hexdigest()
		hidepw = md5(HA1 + ":" + nonce +":" + "00000001" + ":" + "xyz" + ":" + qop + ":" + HA2).hexdigest()
		if hidepw == hash:
			screen_clear()
			time2 = time.time() # stops the 'Clock'
			timetotal = math.ceil(time2 - time1) # Calculates the time taken
			print "\"" + pwd + "\"" + " = " + hidepw + " (in " + str(timetotal) + " seconds)"
			print ""
			return True

if __name__ == '__main__':  # Added this because the multiprocessor module acts funny without it.

    p = Pool(cores)  # Number of processes to create.
    for i in break_points:  # Cycles though the breakpoints list created above.
        a = p.apply_async(pwd_find, kwds=i, args=tuple(), callback=solver)  # This will start the separate processes.
    p.close() # Prevents any more processes being started
    p.join() # Waits for worker process to end

if solved == True:
	end = raw_input("hit enter to exit")
	file.close() # Closes the wordlist file
	screen_clear()
	exit()
else:
	screen_clear()
	time2 = time.time() # Stops the 'Clock'
	totaltime = math.ceil(time2 - time1) # Calculates the time taken
	print "Sorry your password was not found (in " + str(totaltime) + " seconds) out of " + str(length) + " words"
	print ""
	end = raw_input("hit enter to exit")
	file.close() # Closes the wordlist file
	screen_clear()
	exit()
