#Import and create a file
import 4, 6, 5

#ex4 Primme numbers
def is_prime(num):
    if num<=1:
        return False
    if num ==2:
        return  True
    if num % 2 == 0:
        return False
    for i in range (3, int(num**0.5)+1, 2):
        if num % i == 0:
            return False
    return True

n = is_prime(num)
if n == True:
    print(f"{n}numder is prime")
else:
    print(f"{n}numder is not prime")
        

#permutation
from itertools import permutations

def perm(s):
    return list(permutations(s))


a = perm('abc')
for i in a:
    print(i)


#We are ready -> ready are WE (reverse)
def reversed(s = input()):
    return s[::-1]

s = reversed()
print(s)

