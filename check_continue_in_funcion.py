list = [7,8,9,2,5]
sum = 0
for each_elem in list:
	func(each_elem)
print('Here you go')
def func(each_elem):
	print('each element is',each_elem)
	if each_elem == 9:
		continue
	else:
		
		sum += each_elem

print('Here i go')