n, x = [int(x) for x in input().split()]
[print(a, end=' ') for a in [int(a) for a in input().split()] if a < x]