#editor: Nguyen Van Toi
#ask: Reading and Writing Files
from sys import argv
script, filename = argv
print "Nhin nay t mo file %r cho chung may xem." %filename
ofile = open (filename, 'w')

print "Dung 'w' nen phai lam rong file bang truncate"

ofile.truncate()

print "Noi dung can viet vao file:"
line1 = raw_input("line1: ")
line2 = raw_input("line2: ")
line3 = raw_input("line3: ")
print "bat dau ghi file..."
ofile.write(line1)
ofile.write("\t")
ofile.write(line2)
ofile.write("\n")
ofile.write(line3)
print "ok"
ofile.close()

