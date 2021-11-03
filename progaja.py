class Stud:
	def __init__(self,name):
		self.name=name
	def disp(self):
		return self.name
class Batch(Stud):
	def __init__(self,name,rno):
		Stud.__init__(self,name)
		self.rno=rno
	def disp2(self):
		return str(self.rno)+","+self.disp()
s1=Stud("Asakoji")
s2=Batch("Asakoji",10)
print(s1.disp())
print(s2.disp())
