#!/usr/bin/env python3

def return_evens(num_list):
 return [num for num in num_list if num % 2==0]
num_list = range(1,10)
print (num_list)

 
  

def make_exclamation(sentence_list):
 return [sentence + '!' for sentence in sentence_list]
sentence_list = ["Hello", "I'm doing great", "Python is fun"]


print(sentence_list)
    
    
