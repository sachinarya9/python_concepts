class Two:
	def __init__(self,max = 0):
		self.max = max
	def __iter__(self):
		self.n = 0
		return self
	def __next__(self):
		if self.n <= self.max:
			table = 2 * self.n
			self.n +=1
			return table
		else:
			raise StopIteration
			
po = Two(6)
my_iter = iter(po)
# print(next(my_iter))
for i in my_iter:	
	print(i)
	
	
