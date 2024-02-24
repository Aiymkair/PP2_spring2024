#Write a Python program to find the sequences of one upper case letter followed by lower case letters
from re import *
bucvy_str = str(input())

x = findall("[A-Z]+[a-z]+", bucvy_str)

if x:
    print("Matched -", x)
else:
    print("Didn't matched")

