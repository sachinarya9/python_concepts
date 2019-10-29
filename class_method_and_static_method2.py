import datetime
class Employee:
	raise_Amt = 1.5
	
	def __init__(self,first,last,salary):
		self.first = first
		self.last = last
		self.salary = salary
		
	def fullname(self):
		return first + last 
		
	def raise_apply(self):
		self.salary *= self.raise_Amt
		
	@classmethod
	def set_raise_amt(cls,amount):
		cls.raise_Amt = amount
	
	@classmethod
	def fromString(cls,string):
		first,last,salary = string.split('-')
		return cls(first,last,salary)
		
	@staticmethod
	def is_workday(date):
		if date.weekday() == 5 or date.weekday() == 6:
			return False
			
		return True
		
e1 = Employee('Alex','Hales',600000)
e2 = Employee('Andrew', 'flintoff', 1000000)

e1.raise_apply()
e2.raise_apply()
Employee.set_raise_amt(2.5)
print(Employee.raise_Amt)
print(e1.raise_Amt)
print(e2.raise_Amt)
e1.set_raise_amt(2.0)
print(Employee.raise_Amt)
print(e1.raise_Amt)
print(e2.raise_Amt)
e1.raise_Amt = 2.5
print(Employee.raise_Amt)
print(e1.raise_Amt)
print(e2.raise_Amt)
e1.raise_apply()
e2.raise_apply()

print(e1.salary,e2.salary)

e3 = Employee.fromString('alex-hales-4500000')
 
current_date = datetime.date(2019,10,26)
print(e3.is_workday(current_date))