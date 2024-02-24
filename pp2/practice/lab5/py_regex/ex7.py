#Write a python program to convert snake case string to camel case string.
from re import *
bucvy_str = str(input())

x = sub(r"_.", lambda a: a.group()[1].upper(), bucvy_str)
print(x)
