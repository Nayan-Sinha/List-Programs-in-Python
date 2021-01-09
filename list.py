# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 19:20:08 2021

@author: Nayan
"""

#Write a python program that generates a list of 20 random numbers 
#between 1 and 100. Remove the first and last items from the list, 
#sorting the remaining items and print the result.

import random
list=[]
n=int(input("Enter number of elements:"))
for i in range(n):
    list.append(random.randint(1,100)) 
    list.sort()
print('Randomised list is: ',list)
list.pop(0)
list.pop(18)