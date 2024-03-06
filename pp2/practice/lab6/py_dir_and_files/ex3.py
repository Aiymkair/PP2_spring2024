import os 

path = r'C:\Users\ayim0\pp2\PP2_spring2024\pp2\practice\lab6\py_dir_and_files\ex2.py'

if os.path.exists(path):
    print('Path exists')
    print('Filename:', os.path.basename(path))
    print('Directory:', os.path.dirname(path))
else:
    print('This path doesn\'t exist')