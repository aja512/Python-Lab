# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 10:26:37 2019

@author: ajand
"""
def hello(event):
    print("Say Hi")
def bye(event):
     print("Say bye")
     
from tkinter import *
w1=Tk()
b1=Button(w1,text="Click")
b1.pack()
b1.bind("Button1",hello)
b2=Button(w1,text="Click Again")
b2.pack()
b1.bind("Button2",bye)
mainloop()
