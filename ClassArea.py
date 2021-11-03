pi=3.14159256
class A:
	r=0
	#def __init__(self,a):
	#	self.r=float(input("Enter the radius of the circle:"))
	def accept(self):
		self.r=float(input("Enter the radius of circle:"))
	def Area(self):
		print('Area of circle:',pi*self.r**2)

a1=A()
a1.accept()
a1.Area()
