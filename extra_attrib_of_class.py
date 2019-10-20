class complexNumber:
	def __init__(self,imag = 0,real = 0):
		self.imag = imag
		self.real = real
	def getData(self):
		print('{} is {}'.format(self.imag,self.real))

c = complexNumber(6,8)
c.getData()
c.attrib = 60
print(c.attrib)
del c.attrib
print(c.attrib)