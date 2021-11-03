"""
Created on Tue Apr  2 09:18:43 2019

@author: ajand
"""
def square(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return(n*n)

def cube(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return(n*square(n))

def odd(n):
    if (n%2!=0):
        return n

def even(n):
    if (n%2==0):
        return n

def factorial(n):
    if (n==0 or n==1):
        return 1
    else:
        return(n*factorial(n-1))
        
def num_div_by_4(n):
    if (n%4==0):
        return n

