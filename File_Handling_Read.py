"""
Created on Tue Mar 19 09:32:52 2019
@author: Amanda Judy Andrade
"""
def writefile(x):
    i=0    
    for i in range(1,5,1):
        text=input("Enter a string:") 
        x.write(text) 
    x.close()

def openfile():
    x=open("sample.txt",'w')
    return x

x=openfile()
writefile(x)