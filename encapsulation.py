class Computer:
	def __init__(self):
		self.__maxprice =900
	def sell(self):
		print('Price of the computer is {}'.format(self.__maxprice))
	def setMaxPrice(self,Price):
		self.__maxprice = Price
c = Computer()
c.sell()
c.__maxprice = 1000
c.sell()
c.setMaxPrice(1100)
c.sell()		