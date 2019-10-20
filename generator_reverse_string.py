def reverse_str(name):
	length = len(name)
	for char in range(length-1,-1,-1):
		yield name[char]
		
for each_elem in reverse_str('Shubham'):
	print(each_elem)
		