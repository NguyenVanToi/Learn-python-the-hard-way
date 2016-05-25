#editor: Nguyen Van Toi
#ask: Branches and Functions
import math
print "CAC HAM GIAI PHUONG TRINH BAC NHAT VA BAC HAI:"
def bacnhat(a, b):
	if a == 0:
		print "Phuong trinh vo nghiem"
	elif b == 0:
		print "Phuong trinh co nghiem duy nhat la x = 0"
	else: 
		print "Phuong trinh co nghiem duy nhat x = %0.2f" %(-b/a)
def bachai(a, b, c):
	if a == 0:
		bacnhat(b, c)
	else: 
		delta = b*b - 4*a*c
		if delta < 0:
			print "Phuong trinh vo nghiem"
		elif delta == 0:
			print "Phuong trinh co nghiem kep x = %0.2f" %(-b/2*a)
		else: 
			print "Phuong trinh co 2 nghiem phan biet x1 = %0.2f, x2 = %0.2f" %((-b + math.sqrt(delta))/2/a, (-b - math.sqrt(delta))/2/a)		
def start():
	count = int(raw_input("Nhap so cac lan can tinh: "))
	i = 0
	while i < count:
		print "Nhap cac bien dau vao:"
		a = float(raw_input("Nhap a:"))
		b = float(raw_input("Nhap b:"))
		c = float(raw_input("Nhap c:"))
		print "Giai phuong trinh bac nhat vio 2 bien a, b:"
		bacnhat(a, b)
		print "Giai phuong trinh bac hai vio 3 bien a, b, c:"
		bachai(a, b, c)
		i = i + 1
start()



