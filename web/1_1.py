def is_palin(num):
	if num<0:
		num = -num
	return (str(num) == str(num)[::-1])

do_while = 1
while(do_while):
	f = int(input("Введите число: "))
	if is_palin(f):
		print("Ура это палиндром")
	else:
		print("Увы но они разные")
	do_while = (input("Ещё разочек?\n") == 'y')