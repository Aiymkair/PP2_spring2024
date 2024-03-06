import shutil 

shutil.copy('ex4.txt', 'ex7.txt')

with open('ex4.txt', 'r') as file1:
    with open('ex7.txt', 'w') as file2:
        file2.write(file1.read())
        for i in file1: file2.write(i)