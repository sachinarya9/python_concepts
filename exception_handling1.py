import sys
try:
	f = open('test.txt')
	s = f.readline()
	i = int(s.strip())
	
except OSError as err:
	print('OS error: {0}'.format(err))

except Exception as e:
	print('cant convert data to an integer')

except:

	print('Unexpected error:',sys.exc_info()[0])
	raise