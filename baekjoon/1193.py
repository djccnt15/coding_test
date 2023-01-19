n, l = int(input()), 1
while l < n:
    n -= l
    l += 1
a, b = n, l - n + 1
print(f'{a}/{b}' if l % 2 == 0 else f'{b}/{a}')