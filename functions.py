###### Positional argument
def dunc1(name):
	print(name)
	
dunc1('Sachin')

###### Keyword argument

def dunc2(name,age,sex):
	print(name,age,sex)
	
# dunc2('Alex', age = 6, sex = 'm')

dunc2('Alex',6,sex = 'm') # positional argument follows keyword argumnents

###### Default argument

def dunc3(name, age = 35):
	print(name,age)
	
dunc3('Sachin', age=26) # positional argument follows keyword argumnets

def dunc4(*var,age):
	print(var, age)
	for v in var:	
		print(v)
	
dunc4(5,6,7,age =26)

def dunc5(*tup,name1,**info_dict):
	print(tup,info_dict,name1)
	
dict = {'name':'Sachin','age':26}
dunc5(6,7,name1='Sachin',name = 'Sachin',age = 26)

