a, b, v = [int(x) for x in input().split()]
k = (v - b) / (a - b)
print(int(k) if k == int(k) else int(k) + 1)