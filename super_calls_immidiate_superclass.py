# this is multilevel inheritance

class A:
	def __init__(self):
		print('Initializing class A')
		
	def sub_method(self,b):
		print('Printing from class A', b)
		
		
class B(A):
	
	def __init__(self):
		print('Initializing class B')
		super().__init__()
		
	def sub_method(self,b):
		print('printing from class B', b)
		super().sub_method(b+1)
		
		
class C(B):
	
	def __init__(self):
		print('Initializing class C')
		super().__init__()
		
	def sub_method(self,b):
		print('Printing from class C',b)
		super().sub_method(b+1)
	
c = C()
c.sub_method(1)		
		
