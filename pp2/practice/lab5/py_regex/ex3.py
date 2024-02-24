#Write a Python program to find sequences of lowercase letters joined with a underscore
from re import *
bucvy_str = str(input())

x = findall("[a-z]+_[a-z]+", bucvy_str)

if x:
    print("Matched -", x)
else:
    print("Didn't matched")

