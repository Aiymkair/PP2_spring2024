#ex2  Fahrenheit temperature
def fahr_conver(F):
    C = (5 / 9) * (F - 32)
    return C

F=int (input())
C = fahr_conver(F)
print(f"{F}F={C}C")
    