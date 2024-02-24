#Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s
from re import *
bucvy_str = str(input())

x = search("ab*", bucvy_str)

if x:
    print("Matched -", x.group())
else:
    print("Didn't matched")
