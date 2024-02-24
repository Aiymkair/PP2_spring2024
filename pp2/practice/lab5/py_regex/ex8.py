# Write a Python program to split a string at uppercase letters.
from re import *
bucvy_str = str(input())

x = split("[A-Z]+", bucvy_str)
print(x)
