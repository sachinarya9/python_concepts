class Animal:
	def __init__(self):
		print('This is Animal class')
		super().__init__()
		
class Mammal(Animal):
	def __init__(self,animalName):
		print(animalName,'is a mammal')
		super().__init__()
		
class NonMarineMammal(Mammal):
	def __init__(self,animalName):
		print(animalName, 'is a non marine animal')
		super().__init__(animalName)
		
class NonWingedAnimal(Mammal):
	def __init__(self,animalName):
		print(animalName, 'is a non winged animal')
		super().__init__(animalName)
		
class Dog(NonMarineMammal, NonWingedAnimal):
	def __init__(self):
		print('This is a Dog')
		super().__init__('Dog')
		
d = Dog()

print(Dog.__mro__)

b = NonMarineMammal('Bat')
		
	
	