t = [[0 for _ in range(100)] for _ in range(100)]
a = [[int(x) for x in input().split()] for _ in range(int(input()))]
for i, j in a:
    for r in range(i, i + 10):
        for c in range(j, j + 10):
            t[r][c] = 1
print(sum(v for r in t for v in r))


# def add(*a):
#     return [[sum(v) for v in zip(*i)] for i in zip(*a)]


# def mat(r, c):
#     return [[1 if r <= j < r + 10 else 0 for j in range(100)] if c <= i < c + 10 else [0] * 100 for i in range(100)]


# a = [[int(x) for x in input().split()] for _ in range(int(input()))]
# print(sum((bool(v) for m in add(*[mat(x, y) for x, y in a]) for v in m)))