
class Disp:
	x=0
	y=0
	def __init__(self,a,b):
		self.x=a
		self.y=b
	def display(self):
		print(self.x,self.y)
        return self.x+self.y
        
m=int(input("Enter no:"))
n=int(input("Enter no:"))
a1=Disp(m,n)
a1.display()
a1.sum()

