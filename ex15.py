#editor: Nguyen Van Toi
#ask: Reading Files
from sys import argv
script, namefile = argv
txt = open(namefile)
print "Noi dung file  %r la:" %namefile
print txt.read()
nameagain = raw_input("Ten file: ")
txtagian = open(nameagain)
print txtagian.read()
