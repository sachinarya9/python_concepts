def sum(self,a,b):
	return a+b
	
class Calculate:
	sum_new = sum
	
	def sub(self,a,b):
		return a-b
		
	sub_new = sub
	
cal = Calculate()
print(cal.sum_new(6,7))
print(cal.sub_new(7,6))
print(cal.sub(7,6))
print(sum(cal,6,7))