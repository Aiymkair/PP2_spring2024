import os

path = r'C:\Users\ayim0\pp2\PP2_spring2024\pp2\practice\lab6\py_dir_and_files\ex6_folders'

if not os.path.exists(path):
   os.makedirs(path)

A = ord('A')
base = 'ex06_A-Z_files\\{}.txt'
for i in range(A, A+26):
    f = open(base.format(chr(i)), 'w')