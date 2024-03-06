with open('ex5.txt', 'w') as new_file:
    lst = ["anime is much more better than k-dramas"]
    new_file.write(' '.join(map(str, lst)))
    
    new_file.write('\n')
    new_file.writelines(map(str, lst))