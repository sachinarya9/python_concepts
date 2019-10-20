def gene():
	n = 1
	n += 1
	yield n
	
	n += 1
	yield n
	
	
for i in gene():
	
	print(i)
	
	# else:
		# break