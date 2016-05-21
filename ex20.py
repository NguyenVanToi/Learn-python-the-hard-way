#editor: Nguyen Van Toi
#ask: Functions and Files
from sys import argv

script, filename = argv

#ghi du lieu vao file
wfile = open(filename, 'w')
a = """Dong 1 la
Dong 2 la
Dong 3 la
"""
wfile.write(a)
wfile.close()
print "In toan bo du lieu trong file"
def print_all(file):
	r = file.read()
	print r
def vitricontro(file):       #Ham dung de dinh vi tri con tro. seek(0) la dua vi tri con tro len dau file
	file.seek(0)
def print_line(file):		#Ham in 1 dong trong file
	print file.readline()
readfile = open(filename)
print "Doc toan file: "
print_all(readfile)
print "Dua con tro ve dau file bang ham seek()"
vitricontro(readfile)
print "In dong dau tien trong file: "
print_line(readfile)
print "In dong thu 2 trong file: "
print_line(readfile)
print "In dong thu 3 trong file: "
print_line(readfile)
