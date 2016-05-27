import hashmap
country = hashmap.new()
hashmap.set(country, 'VietNam', 'VN')
hashmap.set(country, 'ThaiLan', 'TL')
hashmap.set(country, 'Malaysia', 'ML')
city = hashmap.new()
hashmap.set(country,'VN', 'HaNoi')
hashmap.set(country, 'TL', 'BangKok')
hashmap.set(country, 'ML', 'Kualalumpur')
print "Viet Nam duoc viet gon la: ", hashmap.get(country, 'VietNam')
print "Thu do cua Viet Nam la: ", hashmap.get(city, 'VN')
print "Danh sach: "
hashmap.list(country)
hashmap.list(city)