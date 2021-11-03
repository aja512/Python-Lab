# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 09:37:41 2019

@author: hp
"""
ch=str(object=input("Enter a string: "))
i=0
count=0
for i in ch:
    count+=1
for i in range(0,count,1):
    if ch[i]==ch[count-1]:
        count=count-1
        continue
    else:
        print("Not a palindrome")
        break
    