n, m = [int(x) for x in input().split()]
a = [i + 1 for i in range(n)]

for _ in range(m):
    i, j = [int(x) - 1 for x in input().split()]
    a[i], a[j] = a[j], a[i]

for v in a:
    print(v, end=' ')