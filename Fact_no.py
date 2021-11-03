"""
Created on Tue Apr  2 10:38:04 2019

@author: ajand
"""
fact=1
n=int(input("Enter no. of terms you want to display:"))
for i in range(1,(n+1),1):
    fact=fact*i
print("factorial of a given num=",str(fact))
"""
O/P:-
runfile('H:/AMANDA/SEMESTER 4/PYTHON/PROGRAMS/Fact_no.py', wdir='H:/AMANDA/SEMESTER 4/PYTHON/PROGRAMS')

Enter no. of terms you want to display:5
factorial of a given num= 120
"""