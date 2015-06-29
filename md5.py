import hashlib, time, os
from multiprocessing import Pool

def screen_clear():
	if os.name == 'nt':
		return os.system('cls')
	else:
		return os.system('clear')

screen_clear()

print ""
print "Welcome to the md5 performance test"
print ""

def md5test(word, factor):
    factor = int(factor)
    m = word
    time1 = time.time()
    for number in range(1, factor + 1):
        for number in range(1, 1000001):
            m = hashlib.md5(m).hexdigest()
    time2 = time.time()
    dif = time2 - time1
    dif = round(dif,2)
    print ""
    print word + " hashed " + str(factor) + " million" + " times & took " + str(dif) + " Secconds."
    print ""
    print m

word = raw_input("What word would you like to hash? >> ")

print ""

factor = raw_input("How many million times would you like to hash it >> ")

r = []

for i in range(1,11):
    r.append(str(i))

while factor not in r:
    factor = raw_input("Number must be between 1 and 10. >> ")

md5test(word, factor)

print ""
end = raw_input("hit enter to exit")
screen_clear()
exit()
