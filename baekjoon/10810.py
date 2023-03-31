n, m = [int(x) for x in input().split()]
a = [0] * n

for _ in range(m):
    i, j, k = [int(x) for x in input().split()]
    for n in range(i, j + 1):
        a[n - 1] = k

for v in a:
    print(v, end=' ')