#edtor:Nguyen Van Toi
def hamtach(xau):
	word = xau.split(' ')
	return word

def sort(word):  
	#Ham sap xep theo ki tu tang dan cua cac tu trong word
	return sorted(word) 

def inphantudau(word):
	#Ham in phan tu dau tien trong word da duoc sap xep
	word_first = word.pop(0)
	print word_first

def inphantucuoi(word):
	#Ham in phan tu cuoi trong word da duoc sap xep
	word_last = word.pop(-1)
	print word_last

def sort2(xau):
	#Ham sap xep mot chuoi ki tu bat ki
	word = hamtach(xau)
	return sort(word)

def inphantudaucuoi(xau):
	#Ham in phan tu dau va cuoi cua chuoi khi chua duoc sap xep
	word = hamtach(xau)
	inphantudau(word)
	inphantucuoi(word)

def inphantudaucuoi2(xau):
	#Ham in phan tu dau va cuoi cua chuoi ki tu khi da duoc sap xep
	word = sort2(xau)
	inphantudau(word)
	inphantucuoi(word)
