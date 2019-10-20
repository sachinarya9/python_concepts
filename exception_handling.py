try:
	a = int(input('Enter a number'))
	b = 12
	c = b/a
	print(c)
	
except ZeroDivisionError as e:
	print(e)
	
else:
	print('Else part')
	
finally:
	
	print('finally part')