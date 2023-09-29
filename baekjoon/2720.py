for _ in range(int(input())):
    c = int(input())
    a = []
    c, r = divmod(c, 25)
    a.append(c)
    c, r = divmod(r, 10)
    a.append(c)
    a.extend(divmod(r, 5))
    print(*[str(v) for v in a])