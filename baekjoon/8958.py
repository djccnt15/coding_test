for i in [input().split('X') for _ in range(int(input()))]:
    print(sum(sum(i + 1 for i, _ in enumerate(v)) for v in i))