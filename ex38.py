#editor: Nguyen Van Toi
#ask:  Doing Things to Lists
print "LAM VIEC VOI DANH SACH"
stri = "Toi la mot hoc sinh UET"
stuff = stri.split(' ')
arr_add = ["toi", "hoc", "nganh", "truyen", "thong"]
while len(stuff) < 9:
	word = arr_add.pop()
	print "Them xau %r vao mang arr" %word
	stuff.append(word)
	print "So phan tu trong arr la: %r" %len(stuff)
print "sap xep lai mang: "
sorted(stuff)
print stuff
print "Phan tu dau tien: ", stuff[1]
print "Phan tu cuoi: ", stuff[-1]
print stuff.pop()
print ' '.join(stuff) #noi xau
print '#'.join(stuff[2:5])
