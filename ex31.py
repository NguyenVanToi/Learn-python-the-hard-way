#editor: Nguyen Van Toi
#ask: Making Decisions

print "\tMUC LUC"
chapter = int(raw_input("Moi ban nhap chuong can tim: "))
if chapter == 1:
	print "Ban da truy cap vao chuong %r: TANG UNG DUNG" %chapter
	title = int(raw_input("Moi ban nhap tieu de can tim: "))
	if  title == 1:
		print "Tim hieu ve cac ung dung mang"
	elif title == 2:
		print "Giao thuc HTTP"
	elif title == 3:
		print "Lap trinh socket"
	else: 
		print "Tieu de ban nhap khong ton tai."
elif chapter == 2:
	print "Ban da truy cap vao chuong %r: TANG GIAO VAN" %chapter
	muc = int(raw_input("Moi ban nhap tieu de can tim: "))
	if muc == 1:
		print "Giao thuc TCP va UDP"
	else:
		print "Tong ket chuong."
elif chapter == 3:
	print "Ban da doc het quyen sach roi."
else:
	print "Chuong ban nhap khong ton tai."