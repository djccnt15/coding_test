n, x = [int(x) for x in input().split()]
for a in [int(a) for a in input().split()]:
    if a < x:
        print(a, end=' ')