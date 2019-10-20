class Parent:
	def ParentMethod(self):
		print('calling parent method')
		
class child(Parent):
	def childMethod(self):
		print('calling child method')
		

c = child()
c.childMethod()
c.ParentMethod()	
p = Parent()
p.childMethod()
p.ParentMethod()

		

		