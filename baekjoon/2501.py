n, k = [int(x) for x in input().split()]
try:
    print([x for x in range(1, n + 1) if n % x == 0][k - 1])
except:
    print(0)