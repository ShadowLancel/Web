def rev(num):
	if num<0:
		num = -num
		return (int(str(num)[::-1])) * -1
	return (int(str(num)[::-1]))

while(1):
	s = input("Введите число\n")
	try:
		print(rev(int(s)))
	except:
		break