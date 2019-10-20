c = 2
def smart_divide(func):
	global c
	print('Value of c is',c)
	c = 0
	def inner_func(a,b):
		if b == 0:
			print('We cannot divide a number by 0')
		else:
			print('Hello')
			return func(a,b)
	return inner_func
print('value for c outside is',c)
@smart_divide
def divide(a,b):
	print('Division')
	return a/b
	
print(divide(5,0))