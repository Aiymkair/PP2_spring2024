#Unique elements of first
def unique(l):
    a = []
    for i in l:
        if i not in a: 
            a.append(i)
    return a
if __name__ == "__main__":
    l = list(map(int, input().split()))

    n = unique(l)

    print(n)