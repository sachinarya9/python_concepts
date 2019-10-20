remainder_list = []
num = int(input('eNTER THE UMBER'))
while num != 0:
	print(num)
	remainder_list.append(int(num%2))
	num = int(num/2)

print(remainder_list[::-1])
	