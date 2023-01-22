a = [int(v) for r in [input().split() for _ in range(9)] for v in r]
m = max(a)
i = a.index(m)
print(f'{m}\n{i // 9 + 1} {i % 9 + 1}')