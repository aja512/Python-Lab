n=int(input("Enter no. of terms you want to display:"))
i=0
dig=0
res=0
if n>0:
    while n!=0:
        dig=int(n%10)
        res=res+dig
        n=int(n/10)
    
    print("Sum of Digits=",str(res))
"""
O/P:-
runfile('H:/AMANDA/SEMESTER 4/PYTHON/PROGRAMS/sumofdig.py', wdir='H:/AMANDA/SEMESTER 4/PYTHON/PROGRAMS')

Enter no. of terms you want to display:512
Sum of Digits= 8
"""
