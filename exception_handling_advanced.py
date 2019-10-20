def divide(a,b):
	try:
		result = a/b
		
	except ZeroDivisionError:
		print('division by zero')
		
	else:
		print('Result is', result)
		raise Exception("Re-raise exception")
		
	finally:
		print('Finally got executed')
		
	
divide(2,0)