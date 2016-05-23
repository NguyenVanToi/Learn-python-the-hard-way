#editor: Nguyen Van Toi
#ask:  Functions Can Return Something
def name(myname):
	print "Ten toi la ",  myname
def birthday(age):
	print "#Cach tinh tuoi la 2016 - age."
	return 2016 - age
def tall(a, b):
	print "#Den buoc tinh chieu cao."
	return b - a
def weight(we):
	print "#Dang tinh can nang ..."
	return we

age = int(raw_input("Nhap nam sinh: "))
we = int(raw_input("Can nang cua ban la: "))
tuoi = birthday(age)
chieucao = tall(30, 200)
cannang = weight(we)
print "KET QUA LA: "
name("Nguyen Van Toi")
print "nam nay %r tuoi, cao %r cm, nang %r kg." %(tuoi, chieucao, cannang)
