#editor: Nguyen Van Toi
#ask: Loops and Lists
arr1 = [0, 1, 2, 3, 4, 5]
arr2 = ['khong', 'mot', 'hai', 'ba']
arr3 = ['khong', 1, 'hai', 3, 'bon']

for num in arr1:
	print "Cac phan tu cua arr1 la: %d" %num
for text in arr2:
	print "Cac phan tu cua arr2 la: %s" %text
for ex in arr3:
	print "Cac phan tu cua arr3 la: %r" %ex
arr4 = []
for i in range(0, 6):
	print "Them phan tu %d vao mang arr4." %i
	arr4.append(i)
for i in arr4:
	print "Cac phan tu trong arr4 la: %d" %i
