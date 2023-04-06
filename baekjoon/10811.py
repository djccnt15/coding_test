n, m = [int(x) for x in input().split()]
a = [i + 1 for i in range(n)]

for _ in range(m):
    i, j = [int(x) for x in input().split()]
    a = a[:i-1] + a[i-1:j][::-1] + a[j:]

for v in a:
    print(v, end=' ')