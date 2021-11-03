"""
class shape:
    def __init__(self,length):
        self.length=length
	def disp(self):
		return self.length
"""  
class Square:
    def __init__(self,length):
       self.length=length
    def area(self,length):
        print(self.length*self.length)

class Rectangle(Square):
    def __init__(self,length,breadth):
        super().__init__(length)
        self.breadth=breadth
    def area(self,length,breadth):
        super().area(length)
        return(self.length*self.breadth)
"""
    def disp2(self):
        return(self.Area)
"""        
length=float(input("Enter the length:"))
breadth=float(input("Enter the breadth:"))
a2=Rectangle(length,breadth)
print(a2.area(length,breadth))