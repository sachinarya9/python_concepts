class Car:
	
	cc = 100
	def __init__(self,name,price):
		self.name = name
		self.price = price
		
	def price_and_name(self):
		print(self.price, self.name)
		
	
santro = Car('Santro',200000)
eon = Car('Eon',350000)
price_and_name_copy = santro.price_and_name
print(price_and_name_copy())
print(santro.price_and_name())
print(santro.cc)
santro.cc = 80
print(Car.cc, santro.cc, eon.cc)
Car.cc = 150
print(Car.cc, santro.cc, eon.cc)