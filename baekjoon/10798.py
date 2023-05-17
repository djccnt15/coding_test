print(''.join([''.join(v) for v in [
    r for r in zip(*[list(input().ljust(15, '*')) for _ in range(5)])
]]).replace('*', ''))