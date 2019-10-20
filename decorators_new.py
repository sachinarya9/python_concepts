def smart_divide(func):
	
	def inner(a,b):
		if b == 0:
			print('Cannot divide by 0')
			return
		
		else:
			
			return func(a,b)

	return inner
	
@smart_divide	
def divide(a,b):
	print('value is',a/b)
	return a/b
	
result = divide(4,2)

print(result)