#editor: Nguyen Van Toi
#ask: While Loops

print "Thao tac voi vong lap while."
i = 0
arr = []
while i < 10:
	print "Them phan tu %d vao mang arr." %i
	arr.append(i)
	i = i + 1
print "In mang voi while"
j = 0
while j < 10:
	print arr[j]
	j = j + 1
print "in mang voi for"
for number in arr:
	print number


