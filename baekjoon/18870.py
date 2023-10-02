input()

i = [int(i) for i in input().split()]
d = {v: i for i, v in enumerate(sorted(set(i)))}

print(*[d[e] for e in i])