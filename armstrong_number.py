str_num = input('Enrer a number')
count = len(str_num)
int_num = int(str_num)
added_num = 0
for each_num in str_num:
	added_num = added_num + pow(int(each_num),count)

if added_num == int_num:
	print('Its an armstrong number')