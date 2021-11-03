# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 14:55:53 2019

@author: ajand
"""

print("Enter 'x' for exit.");
string = input("Enter any string to remove all punctuations: ")
if string == 'x':
    exit();
else:
    newstr = string;
    print("\nRemoving punctuations from the given string...");
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~''';
    for x in string.lower():
        if x in punctuations:
            newstr = newstr.replace(x,"");
    print("New string after successfully removing all punctuations\n");
    print(newstr);
