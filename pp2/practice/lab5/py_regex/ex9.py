#Write a Python program to insert spaces between words starting with capital letters.
from re import *
bucvy_str = str(input())

x = sub("[A-Z]", lambda a:f"{a.group(), bucvy_str}")
print(x)
