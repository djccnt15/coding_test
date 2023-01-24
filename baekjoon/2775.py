def people(f, j):
    f[j] += f[j - 1]


def floor():
    a, b = int(input()), int(input())
    f = [i for i in range(1, b + 1)]
    [people(f, j) for _ in range(a) for j in range(1, b)]
    print(f[-1])


[floor() for _ in range(int(input()))]


# def floor():
#     a, b = int(input()), int(input()) + 1
#     f = [[i for i in range(1, b)]]
#     [f.append(list(sum(f[-1][:i]) for i in range(1, b))) for _ in range(a)]
#     print(f[-1][-1])


# [floor() for _ in range(int(input()))]