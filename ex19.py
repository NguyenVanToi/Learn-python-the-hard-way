#editor:Nguyen Van Toi
#ask: Functions and Variables

def total(a, b):
	print "bien a la: %r" %a
	print "bien b la: %r" %b
	print "tong cua 2 so a va b la: %r" %(a + b)

print "Cach 1: "
total(26, 10)
print "Cach 2:"
a, b = 26, 10
total(a, b)
print "Cach 3: "
total(16 + 10, 5 * 2)
print "Cach 4: "
total(a - 0, b / 1)
print "Cach 5: "
c = int(raw_input("Nhap a: "))
d = int(raw_input("Nhap b: "))
total(c, d)