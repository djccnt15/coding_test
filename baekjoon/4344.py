def res(a):
    mean = sum(a) / len(a)
    return round(len([i for i in a if i > mean]) / len(a) * 100, 3)


[print(f'{res(a):.3f}%') for a in [[int(x) for x in input().split()[1:]] for _ in range(int(input()))]]