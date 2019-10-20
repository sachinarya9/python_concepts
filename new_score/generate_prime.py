# num = int(input('Enter a number'))
import data
my_list = []
for num in range(2,20):
	flag = 0
	for i in range(2,num):
		if num%i == 0:
			flag = 1
			break

	if flag == 0:
		my_list.append(num)
print(my_list)
		