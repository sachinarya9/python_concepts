class A:
	def __init__(self):
		print('Initializing: class A')
		super().__init__()
		
	def sub_method(self,b):
		print('Value of b in A is',b)
		super().sub_method(b)
		
class B:
	def __init__(self):
		print('Initializing: class B')
		
	def sub_method(self,b):
		print('Value of b in B is',b+1)
		
class C(A,B):
	def __init__(self):
		print('Initializing: class C')
		super().__init__()
		
	def sub_method(self,b):
		print('Value of b in C is',b)
		super().sub_method(b+1)
		
c = C()
c.sub_method(1)
print(C.__mro__)