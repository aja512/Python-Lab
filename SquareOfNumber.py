class square:
    def __init__(self,x):
		self.x=x
        return(pow(self.x,2))
x=int(input("Enter an integer:"))
A=square(x)
print(A)