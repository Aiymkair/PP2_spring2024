#Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'
from re import *
bucvy_str = str(input())

x = search("a.*b", bucvy_str)

if x:
    print("Matched -", x.group())
else:
    print("Didn't matched")
