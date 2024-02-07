#ex3 Solving a classic puzzle
def solve(numheads, numlegs):
    eq1 = [1, 1]
    eq2 = [numlegs, -1] 
    
    determinant = eq1[0] * eq2[1] - eq1[1] * eq2[0]
    x = (numheads * eq2[1] - numlegs * eq1[1]) / determinant
    y = (numheads * eq2[0] - numlegs * eq1[0]) / determinant

    return int(x), int(y)

numheads = int(input())
numlegs = int(input())
chic , rab = solve(numheads, numlegs)
print(f"{chic} chickens and {rab} rabbits ")