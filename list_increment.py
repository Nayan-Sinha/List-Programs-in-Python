# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 20:31:46 2021

@author: Nayan
"""
#Write a python program to increment numeric string by 6.

string_list = ["hello", "10", "i", "100", "am", "Nayan", "123"]   
print("The Numeric string list is : " + str(string_list)) 
I = 6  
res = [] 
for ele in string_list:   
    if ele.isdigit(): 
        res.append(str(int(ele) + I)) 
    else: 
        res.append(ele) 
print("Incremented Numeric Strings : " + str(res))