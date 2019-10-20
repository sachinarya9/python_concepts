def my_exception(data):
	if ':' in data:
		raise Exception("Invalid data",data)
	return data


try:
	my_exception('Name : Alex')
	print('Ohh yeah')
	
except Exception as e:
	print('exception occured',e.args[0],e.args[1])
		