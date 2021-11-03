count=0
i=0
x=int(input("Enter the integer you want to search:"))
ls=[12,512,2048,206,54,5,512]
for i in ls:
	if x==i:
		count=count+1
		print("Value",str(x),"found !")
	else:
		print("Value",str(x),"not present in List")
print("Occurences=",str(count))
