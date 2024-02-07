#Volume of a sphere
import math
def aiym(r):
    return 4/3 * math.pi * pow(r, 3)

if __name__ == "__main__":
    r = int(input())
    print(f'Volume = {aiym(r)}')