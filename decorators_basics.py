def my_gen():
	n = 1
	print('This is the first line')
	yield n
	
	n +=1
	print('This is the second line')
	yield n
	
	n+=1
	print('This is the third line')
	yield n
	
a = my_gen()
# for i in a:
	# print(i)
	
print(next(a))
print(next(a))
print(next(a))
print(next(a))