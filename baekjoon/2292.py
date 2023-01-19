i = int(input())
n, c = 1, 1
while i > n:
    n += 6 * c
    c += 1
print(c)