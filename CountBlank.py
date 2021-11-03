L: object=str(object=input("Enter a string:"))
cn=L.count(" ")
flag=0
words=0
for i in L:
	if i==" ":
		flag=1
		if flag==1:
			words=words+1
			flag=0	
		else:
			continue

print("No. of Blank Spaces:",cn)
print("No. of words:",words)
