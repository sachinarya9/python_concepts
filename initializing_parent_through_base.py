class Computer:
	def __init__(self,ram,hdd):
		self.ram = ram
		self.hdd = hdd
	
class Laptop(Computer):
	def __init__(self,ram,hdd,model_name):
		super().__init__(ram,hdd)
		self.model_name = model_name
		

dell = Laptop(6,1,'Dell Vestro')
print('Ram of the computer is',dell.ram)
print('Hard disk of the computer is',dell.hdd,'GB')
print('Model name of the computer is',dell.model_name)