class Animal:
	def __init__(self,name):
		print(name, 'is a warm blooded animal')
		
	
class Dog(Animal):
	def __init__(self,name):
		print('This is a Dog')
		super().__init__(name)
		
		
d = Dog('Dog')