def decorate(func):
	def inner(a,b):
		if b == 0:
			print('Sorry we cannot divide any number by 0')
			return
		else:
			print('came here')
			# return func(a,b)
			c = a/b
			print(c)
	return inner		

@decorate
def divide(a,b):
	return a/b
# print(divide(8,4))
divide(8,4)