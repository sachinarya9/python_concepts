from datetime import date

class Person:
	def __init__(self, name,age):
		self.name = name
		self.age = age
		
	@classmethod
	def calculate_age(cls,name, year):
		age = date.today().year - year
		return cls(name,age)
		
	@staticmethod
	def valid_age(x):
		print('x is',x)
		if x>18:
			print('eligible to vote')
		
p = Person('Sachin',26)

p1 = Person.calculate_age('Kapil',1994)

p1 = p.calculate_age('Akash',1991) # if you call class method 'calculate_age' through an already existing instance variable p, then also p1 instance will be formed without any error, without changing the attributes of the instance variable 'p', i.e through p we are calling class method 'calculate_age' to make a new object, but the attributes in the instance variable 'p' will remain the same as they they were earlier and will not be change i.e name will be 'Sachin' and age will be 26

print('age is',p1.age) 

print('age is',p.age) # altough p is a different object with different values of 

p1.valid_age(p1.age)
# if you call class method 'calculate_age' through an already existing instance variable p, then also p1 instance will be formed without any error, without changing the attributes of the instance variable 'p', i.e through p we are calling class method 'calculate_age' to make a new object, but the attributes in the instance variable 'p' will remain the same as they they were earlier and will not be change i.e name will be 'Sachin' and age will be 26