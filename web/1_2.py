def get_ls(nums):
	l_2 = list()
	l_3 = list()
	l_5 = list()
	for num in nums:
		if ((num % 2) == 0):
			l_2.append(num)
		if ((num % 3) == 0):
			l_3.append(num)
		if ((num % 5) == 0):
			l_5.append(num)
	return (l_2, l_3, l_5)

l_nums = []
while(1):
	s = input("Введите число\n")
	try:
		l_nums.append(int(s))
	except:
		break
result = get_three_list(l_nums)
print(result[0])
print(result[1])
print(result[2])