n = [int(input()) for _ in range(28)]
for a in sorted(a for a in range(1, 31) if a not in n):
    print(a)