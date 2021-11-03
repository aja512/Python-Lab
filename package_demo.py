# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 09:22:45 2019

@author: ajand
"""
import FiveCalculateMethods as fcm

n=int(input("Enter an integer:"))

z=fcm.square(n)
x=fcm.cube(n)
i=0
j=0
k=0
print("Squared integer=",str(z))
print("Squared integer=",str(x))
print( )
print("Odd nos:-")
for i in range(1,(n+1),2):
    y=fcm.odd(i)
    print(y)
    
print("\n")
print("Even numbers:")
for j in range(1,(n+1)):
    a=fcm.even(j)
    print(a)
f=fcm.factorial(n)
print("Factorial=",str(f))

for k in range(1,(n+1)):
    fou=fcm.num_div_by_4(k)
    print(fou)
"""
O/P:-
runfile('H:/AMANDA/SEMESTER 4/PYTHON/package_demo.py', wdir='H:/AMANDA/SEMESTER 4/PYTHON')
Reloaded modules: FiveCalculateMethods

Enter an integer:12
Squared integer= 144
Squared integer= 1728

Odd nos:-
1
3
5
7
9
11


Even numbers:
None
2
None
4
None
6
None
8
None
10
None
12
Factorial= 479001600
None
None
None
4
None
None
None
8
None
None
None
12
"""