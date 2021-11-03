# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 14:50:56 2019

@author: ajand
"""

# Function to sort the words 
# in ascending order 
def sortedSentence(Sentence): 
      
    # Spliting the Sentence into words 
    words = Sentence.split(" ") 
      
    # Sorting the words 
    words.sort() 
      
    # Making new Sentence by  
    # joining the sorted words 
    newSentence = " ".join(words) 
      
    # Return newSentence 
    return newSentence 
  
# Driver's Code 
  
Sentence = "to learn programming refer geeksforgeeks"
# Print the sortedSentence 
print(sortedSentence(Sentence)) 
  
Sentence = "geeks for geeks"
# Print the sortedSentence 
print(sortedSentence(Sentence)) 
