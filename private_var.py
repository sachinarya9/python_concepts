class PriVar:
	__secretcontent = 0
	_temp = 0
	
	def count(self):
		self.__secretcontent += 1
		return self.__secretcontent
	
count1 = PriVar()
count2 = PriVar()

print(count2.count())

count2.__secretcontent = 100

print('counter is',count2.__secretcontent)

print(count2.count())

print(count2._temp)

print(count2._PriVar__secretcontent)

print(count1.count())

print(count1._PriVar__secretcontent)

