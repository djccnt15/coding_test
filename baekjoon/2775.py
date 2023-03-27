def people(f, j):
    f[j] += f[j - 1]


def floor():
    a, b = int(input()), int(input())
    f = [i for i in range(1, b + 1)]
    for _ in range(a):
        for j in range(1, b):
            people(f, j)
    print(f[-1])


for _ in range(int(input())):
    floor()


# def floor():
#     a, b = int(input()), int(input()) + 1
#     f = [[i for i in range(1, b)]]
#     for _ in range(a):
#         f.append(list(sum(f[-1][:i]) for i in range(1, b)))
#     print(f[-1][-1])


# for _ in range(int(input())):
#     floor()