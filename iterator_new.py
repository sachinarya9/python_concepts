class iterator1:
	
	def __init__(self,data):
		self.data = data
		self.index = len(data)
		
	def __iter__(self):
		return self
		
	def __next__(self):
		if self.index == 0:
			raise Stopiteration
		self.index -= 1
		return self.data[self.index]
		
i = iterator1('King')
a = iter(i)
print(next(a))

for element in i:
	print(element)