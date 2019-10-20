class Employee:
	empcount = 0
	def __init__(self,name,sal):	
		self.name = name 
		self.sal = sal
		# self.empcount = 6
		self.empcount += 1
		
	def getdata(self):
		return self.name, self.sal
		
	def total_employees(self):
		return Employee.empcount
		
e1 = Employee('Ankit Sharma',50000)

e2 = Employee('Vaibhav Joshi',60000)

print(e2.total_employees(),e2.empcount, Employee.empcount)
