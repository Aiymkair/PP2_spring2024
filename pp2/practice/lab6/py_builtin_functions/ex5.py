def f(num, a):
    print(f'tuple #{num} is {all(a)}')


t1 = (True, True, True, True)
t2 = (True, True, False, False)

f(1, t1)
f(2, t2)