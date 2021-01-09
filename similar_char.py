# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 22:20:33 2021

@author: Nayan
"""
#Write a python program to filter all the strings 
#which have a similar case , either upper or lower (Palindrome type)

list1 = ["nayan", "DAD", "abcd", "Java", "mom"]
print("Orginal list of strings:")
print(list1) 
result = list(filter(lambda x: (x == "".join(reversed(x))), list1)) 
print("\nList of similar character:")
print(result)