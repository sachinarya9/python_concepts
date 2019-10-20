class MultiplyByZero(Exception):
	
	def __init__(self,a):
		self.a = a
		
		print('cANT MULTIPLY this')	
	# def check():
		# if self.a == 0:
			# raise Exception('Cannot multiply by 0')
	
		# return self.a
		
try:
	a = int(input('Enter a number'))
	
	b = a*5
	if a == 0:
		raise MultiplyByZero(a)
	print(b)
	
except MultiplyByZero as e:
	print('Cant multiply',e)

except:
	print('Exception')
	
