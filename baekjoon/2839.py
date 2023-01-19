n, b = int(input()), 0
while n % 5:
    n -= 3
    b += 1
print(-1 if n < 0 else n // 5 + b)