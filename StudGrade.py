# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 14:15:15 2019

@author: ajand
"""

x=int(input("Enter marks of subject :"))


if (x>85):
    print ("Grade is A")
else:
    if (x>70):
        print ("Grade is B")
    else:
        if (x>60):
            print ("Grade is C")
        else:
            if (x>35):
                print ("Grade is D")
            else:
                print ("Grade is F")
