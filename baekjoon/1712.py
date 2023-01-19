a, b, c = [int(x) for x in input().split()]
print(-1 if b >= c else int(a / (c - b)) + 1)