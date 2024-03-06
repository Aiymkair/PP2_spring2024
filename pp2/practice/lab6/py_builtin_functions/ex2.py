ai = input()
upper = list(filter(lambda x: x.isupper() , ai))
lower = list(filter(lambda x: x.islower(), ai))

print(f'{len(lower)} - lowercase letters\n{len(upper)} - uppercase letters')
