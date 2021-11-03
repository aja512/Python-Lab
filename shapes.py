class shapes:
	Count_Cylinder=0
	Count_Cone=0	
	def __init__(self,rad,height):
		self.rad=rad
		self.height=height
	def disp(self):
		return self.rad+","+self.height
class Cone(shapes):
	def __init__(self,rad,height):
		shapes.__init__(self,rad,height)
		self.slen=pow((pow(self.rad,2)+pow(self.height,2)),0.5)
		self.Vol=(3.141592*pow(self.rad,2)*self.height)/3
		self.SA=3.141592*self.rad*self.slen
		shapes.Count_Cone=shapes.Count_Cone+1	
	def disp2(self):
		return self.Vol,self.SA,shapes.Count_Cone
class Cylinder(shapes):
	def __init__(self,rad,height):
		shapes.__init__(self,rad,height)
		self.Vol=3.141592*pow(self.rad,2)*self.height
		self.SA=3.141592*(self.rad*self.height+2*self.rad)
		shapes.Count_Cylinder=shapes.Count_Cylinder+1
	def disp3(self):
		return self.Vol,self.SA,shapes.Count_Cylinder
rad=float(input("enter the radius:"))
height=float(input("enter the height:"))
s1=Cone(rad,height)
s2=Cylinder(rad,height)
s3=Cylinder(rad,height)
print("Volume & Total Surface Area of Cone:")
print(s1.disp2())
print("Volume & Total Surface Area of Cylinder:")
print(s2.disp3())
print(s3.disp3())

