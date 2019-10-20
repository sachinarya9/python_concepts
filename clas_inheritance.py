class Bird:
	def __init__(self,name,age):
		self.name = name
		self.age = age
	def whoisthis():
		print('Bird')
	def swim():
		print('Swim faster')
class Penguin(Bird):
	def __init__(self,name,age):
		print('This is a Penguin')
		super.__init__(self,name,age)
	def whoisthis():
		print('Penguin')
	def run():	
		print('Run faster')

peng = Penguin('Penguin',22)
peng.whoisthis()