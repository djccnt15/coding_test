d = [int(input()) for _ in range(28)]
[print(a) for a in sorted(a for a in range(1, 31) if a not in d)]