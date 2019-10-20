class Parrot:
	def fly(self):
		print(' Parrot can fly')
	def swim(self):
		print('Parrot can swim')

class Penguin:
	def fly(self):
		print('Penuin cannot fly')
	def swim(self):
		print('Penguin cannot swim')

def flying(obj):
	obj.fly()
	obj.swim()

p = Parrot()
pen = Penguin()
flying(p)
flying(pen)