import armstrong_number

class Parrot:
	species = 'Bird'
	def __init__(self,name,age):
		self.name = name
		self.age = age
	def sing(self, song):
		return song
p = Parrot('Bird',5)

print('{} is {} years old.'.format(p.name,p.age))
print('Song is {}'.format(p.sing('Happy')))
print('Species is {}',p.__class__.species)
print(p.species)