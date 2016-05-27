#editor: Nguyen Van Toi
#ask: Bang bam Hash map
Tham khao ma nguon tai http://learnpythonthehardway.org/book/ex39.html
def new(solg = 256):
	aMap = [] #Khoi tao mang bam
	for i in range(0, solg):
		aMap.append([]) #Khoi tao cac phan tu trong cua mang
	return aMap
#Tao key cho 1 phan tu
def hash_key(aMap, key):
	return hash(key) % len(aMap) #key duoc tao ra se la 1 so sau do no se chuyen thanh 1 chi so cho bucket
def get_bucket(aMap, key):
	bucket_id = hash_key(aMap, key) #Voi 1 key chung ta co the tim duoc bucket noi ma no se den
	return aMap[bucket_id]
#Ham se tra ve chi so, key, value cua 1 slot tim thay trong bucket, neu khong tra ve -1
def get_slot(aMap, key, default = None):
	bucket = get_bucket(aMap, key)
	for i, kv in enumerate(bucket):
		k, v = kv
		if key == k:
			return i, k, v
	return -1, key, default
#Ham tra ve gia tri value tuong ung voi key
def get(aMap, key, default = None):
	i, k, v = get_slot(aMap, key, default = default)
	return v
#Ham cai dat key, value neu nhu key ton tai thi thay the
def set(aMap, key, value):
	bucket = get_bucket(aMap, key)
	i, k, v = get_slot(aMap, key)
	if i >= 0: #bucket da ton tai
		bucket[i] = (key, value)
	else:
		bucket.append((key, value))
#Ham xoa 1 key torng the Map
def delete(aMap, key):
	bucket = get_bucket(aMap, key)
	for i in xrange(len(bucket)):
		k, v = bucket[i]
		if key == k:
			del bucket[i]
		 	break
#Ham in ra danh sach cac bucket
def list(aMap):
	for bucket in aMap:
		if bucket:
			for k, v in bucket:
				print k ,v		 	
