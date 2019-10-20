class number(object):
	def __init__(self):
		pass
		
	def number(Self):
		print('first yes')

class zeroth(number): # single inheritance
	def __init__(self):
		pass
		
	def number(self):
		print('yes')
		
class first(zeroth): # multilevel inheritance number->zeroth->first
	def __init__(self):
		pass
		
	def number(self):
		print('oh yes')
		
		
class Second(first): 
	def __init__(self):
		pass
		
	def number(self):
		print('second')
		
class Third(first): # hierarichal inheritance first-> second,third
	def __init__(self):
		pass
		
	def number(self):
		print('fourth')
		
class Fourth(Second, Third):
	def __init__(self):
		pass
		
	def number(self):
		print('fourth')
		
obj = Fourth()

print(obj.number())
print(Fourth.__mro__)
		
		

		
		