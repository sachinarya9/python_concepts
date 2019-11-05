import logging

logging.basicConfig(filename = 'test.log', level = logging.DEBUG, format = '%(asctime)s :%(levelname)s: %(name)s %(message)s')

def add(a,b):
	return a+b
	
	
a = 5
b = 3

add_result = add(a,b)
logging.debug('Add: {} + {} = {}'.format(num_1, num_2, add_result))