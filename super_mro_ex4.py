class Zeroth:
	def __init__(self):
		print('zeroth')
		# super().__init__()
		
class First:
	def __init__(self):
		print('First')
		super().__init__()
		
class Second(Zeroth):
	def __init__(self):
		print('sECOND')
		super().__init__()
		
class Third(First):
	def __init__(self):
		print('Third')
		super().__init__()
		
class Fourth(Second,Third):
	def __init__(self):
		print('Fourth')
		super().__init__()
		
f = Fourth()
print(Fourth.__mro__)
	