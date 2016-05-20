#editor: Nguyen Van Toi
#ask: Prompting and Passing
from sys import argv
namefile, username =  argv
print "Day la file cua ", username
print "Ten file la %s" %(namefile)
live = raw_input("Que cua thagn viet ra file nay: ")
date = raw_input("Ngay sinh: ")
print "No la %r,  que %r, ngay sinh %r" %(username, live, date)