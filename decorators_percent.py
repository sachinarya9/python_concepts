def percent(func):
	def inner(*args,**kwargs):
		print('%'*30)
		func(*args,**kwargs)
		print('%'*30)
	
	return inner

def star(func):
	def inner(*args,**kwargs):	
		print('*'*30)
		func(*args,**kwargs)
		print('*'*30)
		
	return inner	

@star
@percent	
def printer(a):
	print(a)
	
printer('Hey man')