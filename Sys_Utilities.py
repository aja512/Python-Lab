"""
Created on Tue Mar 19 09:32:52 2019
@author: Amanda Judy Andrade
"""
from shutil import copyfile
print("File Contents:")
f1=open("sample.txt",'r+')
sr=f1.read(100)
f2=open("sample1.txt",'w+')
copyfile("sample.txt","sample1.txt")
f2=open("sample1.txt",'r+')
sr=f1.read(100)
f1.close()