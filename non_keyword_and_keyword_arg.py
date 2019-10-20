# def arg_function(*args,**kwargs):
	# print(args)
# arg_function()

def star(func):
	def inner(*args,**kwargs):
		print("*"*30)
		func(*args,**kwargs)
		print("*"*30)
	return inner
	
def percent(func):
	def inner(*args,**kwargs):
		print("%"*30)
		func(*args,**kwargs)
		print("%"*30)
	return inner
@star
@percent
def printer(msg):
	print(msg)
	
printer('I will do it')

