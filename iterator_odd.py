class Infilter:
	def __init__(self,max = 0):
		self.max = max
	def __iter__(self):
		self.n = 1
		return self
	def __next__(self):
		if self.n <= self.max:
			odd_value = self.n + 2
			self.n += 2
			return odd_value
		else:
			raise StopIteration

inf = Infilter(10)
infy = iter(inf)
for i in infy:
	print(i)