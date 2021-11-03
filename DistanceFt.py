class Calcu:
	ft=0
	inc=0
	def accept(self):
		print("enter distance in ft & inches")
		self.ft1=int(input())
		self.inc1=int(input())
		
		print("enter distance in ft & inches")
		self.ft2=int(input())
		self.inc2=int(input())
		
	def add(self):
		ft=self.ft1+self.ft2
		inc=self.inc1+self.inc2
		while inc>12:
			ft=ft+1
			inc=inc-12
		print("distance in ft & inches:",ft,",",inc)
a1=Calcu()
a1.accept()
a1.add()
