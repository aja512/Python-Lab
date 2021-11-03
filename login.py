
# import everything from tkinter module 
from tkinter import *
  
# globally declare the expression variable 
expression = "" 
  
# Driver code 
if __name__ == "__main__": 
    # create a GUI window 
    gui = Tk() 
  
    # set the background colour of GUI window 
    gui.configure(background="magenta") 
  
    # set the title of GUI window 
    gui.title("Simple Calculator") 
  
    # set the configuration of GUI window 
    gui.geometry("265x125") 
  
    # StringVar() is the variable class 
    # we create an instance of this class 
    equation = StringVar() 
  
    # create the text entry box for 
    # showing the expression . 
    expression_field = Entry(gui, textvariable=equation) 
  
    # grid method is used for placing 
    # the widgets at respective positions 
    # in table like structure . 
    expression_field.grid(columnspan=4, ipadx=70) 
  
    equation.set('enter your expression') 
  
    # create a Buttons and place at a particular 
    # location inside the root window . 
    # when user press the button, the command or 
    # function affiliated to that button is executed . 
    w=Label(master=gui,cnf={},**)
    button1 = Button(gui, text=' 1 ', fg='black', bg='red', 
                     command=lambda: equalpress(1), height=1, width=7) 
    button1.grid(row=2, column=0) 
  
    
  
  
  
    # start the GUI 
    gui.mainloop() 