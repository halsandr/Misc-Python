import hashlib, time, os

t = 0
n = 0
w = "Hello world"
m = w

def screen_clear():
	if os.name == 'nt':
		return os.system('cls')
	else:
		return os.system('clear')

screen_clear()

print "Welcombe to the hash timer"
print ""

start = raw_input("How many secconds? ")
while start.isdigit() == False:
	start = raw_input("Please enter a number ")
start = int(start)

print ""

screen_clear()

print "Please wait"

time1 = time.time()

while t < start:
	m = hashlib.md5(m).hexdigest()
	time2 = time.time()
	t = time2 - time1
	n = n + 1
	
screen_clear()

if t > 1:
	print "In %s Secconds" % start
else:
	print "In %s Seccond" % start
	
print "you were able to hash '%s' %i Times" % (w, n)
print "this produced the hash %s" % m
