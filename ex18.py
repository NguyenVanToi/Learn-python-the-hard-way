#editor: Nguyen Van Toi
#ask:Names, Variables, Code, Functions
def print_1(*args):
	var1, var2 = args
	print "var1: %r, var2: %r" %(var1, var2)
def print_2(var1, var2):
	print "var1: %r, var2: %r" %(var1, var2)
def print_3(one):
	print "print: %r" %one
def print_4():
	print "Thich gi in day @@"
print_1("toi", "tuan")
print_2("toi", "Thao")
print_3("toi")
print_4()
