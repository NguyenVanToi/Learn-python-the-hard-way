#editor: Nguyen Van Toi
#ask:  More Practice
print " Day la bai tap on lai tat ca kien thuc da hoc"
def market(soluong):
	jean = 50 * soluong
	Tshirt = 20 * soluong
	coat = 100 * soluong
	shose = 25 * soluong
	return jean, Tshirt, coat, shose
soluong =  int(raw_input("Nhap so luong: "))
jean, Tshirt, coat, shose = market(soluong)
print """
	Tong gia tung san pham la:
	- jean = %d
	-Tshirt = %d
	- coat = %d
	- shose = %d
	""" %(jean, Tshirt, coat, shose)
print "Tong la: %d" %(jean + Tshirt + coat + shose)
