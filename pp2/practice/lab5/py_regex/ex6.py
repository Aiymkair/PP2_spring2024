#Write a Python program to replace all occurrences of space, comma, or dot with a colon.
from re import *
bucvy_str = str(input())

x = sub('[\s,.]',':', bucvy_str)

print('Result:\n', x)
