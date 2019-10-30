class A:
	def foo(self,x):
		print('This is my first class and static method class', self, x)
		
	@classmethod
	def class_method(cls,x):
		print('class method',cls,x)
		
	@staticmethod
	def static_method(x):
		print('static method',x)
		
		
a = A()
a.foo('game')
# A.foo() # this will goven an error foo() missing 1 required positional argument: 'self', because we cannot call function belonging to an instance variable with class name.
A.foo('game')

# these changes were done by Sachin Arya.