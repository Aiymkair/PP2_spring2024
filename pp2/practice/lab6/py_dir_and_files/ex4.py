import os

path = r'C:\Users\ayim0\pp2\PP2_spring2024\pp2\practice\lab6\py_dir_and_files\ex4.txt'

with open(path, 'r') as f:
    lines = f.readlines()
    print('Number of lines in {}: {}'.format(os.path.basename(path), len(lines)))