import time, os
from passlib.hash import pbkdf2_sha256

def screen_clear():
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')

screen_clear()

print ""
print "Welcome to the pbkdb2_sha256 performance test"
print ""

def pbkdf2(word, factor):
    time1 = time.time()
    factor = int(factor)
    m = word
    m = pbkdf2_sha256.encrypt(m, rounds=factor, salt_size=16)
    time2 = time.time()
    dif = time2 - time1
    print ""
    print "The word " + word + " hashed " + str(factor) + " times & took " + str(dif) + " Secconds"
    print ""
    print m

word = raw_input("What word would you like to hash? >> ")
print ""
factor = raw_input("What factor would you like to hash it >> ")

pbkdf2(word, factor)

print ""
end = raw_input("hit enter to exit")

screen_clear()

exit()
