#Write a Python program to convert a given camel case string to snake case.
from re import *
bucvy_str = str(input())

x = sub(r".[A-Z]", lambda a:f"{a.group().lower()[0]}_{a.group().lower()[1]}", bucvy_str)
print(x)
