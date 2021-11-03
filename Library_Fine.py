# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 14:30:09 2019

@author: ajand
"""

def permanent():
	a=int(input("No. of day extended :"))
	b=int(input("No. of day extended :"))
	fine=y*10
	print("Total fine = ",fine )

def temporary():
    a=int(input("No. of day extended :"))
	b=int(input("No. of day extended :"))
	fine=y*20
	print("Total fine = ",fine )

def damage():
	fine=0
	y=int(input("No. of books damaged :"))
	fine=y*50
	print("Total fine = ",fine )

def lost():
	fine=0
	y=int(input("No. of books :"))
	fine=y*150
	print("Total fine = ",fine)

x=input("Enter the type :\n1.Permanent worker\n2.Temporary worker\nEnter your choice :")

if x==1:
	permanent()
elif x==2:
	temporary()
else:
	print("INVALID INPUT")
