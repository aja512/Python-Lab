# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 14:46:27 2019

@author: ajand
"""

string=str(object=input("Enter string:"))
vowels=0
for i in string:
      if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
            vowels=vowels+1
print("Number of vowels are:",vowels)
