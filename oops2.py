class Car:
	cc = 100
	def __init__(self,name,ccc,price):
		self.name = name
		self.ccc = ccc
		self.price = price
		
	def price_inc(self):
		self.price = self.price * 1.15
		return self.price
c1 = Car('Honda',500,1000000)
c2 = Car('Accent',600,1100000)
print('Name is',c1.name)
print(c1.price_inc())
c1.cc = 600
print('cc is',c1.cc, Car.cc)
Car.cc = 500
print('cc is',c1.cc, Car.cc)