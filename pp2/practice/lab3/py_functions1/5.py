#permutation
from itertools import permutations

def perm(s):
    return list(permutations(s))


a = perm('abc')
for i in a:
    print(i)





