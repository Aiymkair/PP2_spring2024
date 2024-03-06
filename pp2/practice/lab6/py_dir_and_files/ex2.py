import os 

path = 'C:/Users/ayim0/pp2/PP2_spring2024/pp2/practice/lab3'
print('Exists:', os.access(path, os.F_OK))
print('Access to read:', os.access(path, os.R_OK))
print('Access to write:', os.access(path, os.W_OK))
print('Can be executed:', os.access(path, os.X_OK))