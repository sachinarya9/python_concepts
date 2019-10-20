class Polygon:
	def __init__(self, no_of_sides):
		self.no_of_sides = no_of_sides
		# self.sides = [0 for i in range(no_of_sides)]
	def inputSides(self):
		self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.no_of_sides)]
	def dispSides(self):
		for i in range(self.no_of_sides):
			print(self.sides[i]) 
			
class Triangle(Polygon):
	def __init__(self, no_of_sides):
		super().__init__(no_of_sides)
	
	def findArea(self):
		a,b,c = self.sides
		s = a+b+c/2
		area = (s*(s-a)*(s-b)*(s-c))
		print('Area is',area)
p = Polygon(5)
p.inputSides()
p.dispSides()
print(p.sides)

# for Triangle
t = Triangle(3)
t.inputSides()
t.findArea()