#Write a Python program that matches a string that has an 'a' followed by two to three 'b'
from re import *
bucvy_str = str(input())

x = search(r"ab{2,3}", bucvy_str)

if x:
    print("Matched -", x.group())
else:
    print("Didn't matched")
