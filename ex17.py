#editor: Nguyen Van Toi
#ask More files
from sys import argv

from os.path import exists

script, filegui, filenhan = argv
#ghi du lieu vao file gui
wfile = open(filegui, 'w')
data = raw_input("Du lieu can ghi: ")
wfile.write(data)
wfile.close()
readfile = open (filegui)
rfile = readfile.read()
print "Do dai cua file %r" %(len(rfile)) #tinh do dai file(don vi la byte)
print "Kiem tra xem file da ton tai chua: %r" % (exists(filenhan))
#chuyen du lieu sang file nhan
out = open(filenhan, 'w')
out.write(data)
print "ok"
readfile.close()
out.close()
