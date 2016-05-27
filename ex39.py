#editor: Nguyen Van Toi
#ask: Dictionaries, Oh Lovely Dictionaries
print "TU DIEN"
country = {'VietNam': 'VN', 'Thailan': 'TL', 'Malaysia': 'ML'}
city = {'VN': 'HaNoi', 'ML': 'Kualalumpur'}
#tao them phan tu trong tu dien
city['TL'] = 'Bangkok'
print "Thu do cua Viet Nam la: ", city['VN']
print "Thu do cua Thai Lan la: ", city['TL']
print "\nViet Nam duoc viet gon la: ", country['VietNam']
print "Malaysia duoc viet gon la: ", country['Malaysia']
print "\n1 cach truy xuat du lieu khac:"
print "Thu do Viet Nam la: ", city[country['VietNam']]
print "\nDung vong lap: "
for a, b in country.items():
	print "%s duoc viet gon la: %s" %(a, b)
for c, d in city.items():
	print "Thu do cua %s la: %s" %(c, d)
