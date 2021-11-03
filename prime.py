i=2
n=int(input("Enter an Integer:"))
if n==1:
	print("1 isn't prime nor Composite")
else:
	while(n%i!=0):
		i=i+1
	if n==i:
		print(n,"Is prime")
	else:
		print(n,"Is Composite")
