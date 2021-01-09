# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 20:58:49 2021

@author: Nayan
"""
#Write a program to find the sum of characters ASCII values in string list.

str1 = input("Enter your String : ")
li=[] 
li[:0]=str1 
print(li)
result=[]
for i in range(len(li)):
    result.append(ord(li[i]))
    result = list(set(result))
print(result)   
final=sum(result) 
print("The sum of the your string '{}'is: {}".format(str1,final))
