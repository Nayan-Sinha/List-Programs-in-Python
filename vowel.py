# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 21:45:54 2021

@author: Nayan
"""
#Write a program to print element with maximum vowels from a list.

list1=input("Enter string:")
vowels=0
for i in list1:
      if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
            vowels=vowels+1
print("Number of vowels are:")
print(vowels)