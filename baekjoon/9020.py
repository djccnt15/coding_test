def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


for _ in range(int(input())):
    n = int(input())
    a = b = n // 2
    while a > 0:
        if is_prime(a) and is_prime(b):
            print(a, b)
            break
        a -= 1
        b += 1


# def prime(n):
#     d = [i for i in range(2, n + 1)]
#     c = {j for i in range(2, int(n ** 0.5) + 1) for j in range(i * 2, n + i, i)}
#     return [v for v in d if v not in c]


# for i in range(int(input())):
#     n = int(input())
#     l = prime(n)
#     a = n // 2
#     while a > 0:
#         if a in l and n - a in l:
#             print(a, n - a)
#             break
#         a -= 1


# from itertools import combinations_with_replacement


# def prime(n):
#     d = [i for i in range(2, n + 1)]
#     c = {j for i in range(2, int(n ** 0.5) + 1) for j in range(i * 2, n + i, i)}
#     return [v for v in d if v not in c]


# for _ in range(int(input())):
#     n = int(input())
#     l = list(combinations_with_replacement(prime(n), 2))
#     for x in [l[i] for i, x in enumerate(l) if sum(x) == n][-1]:
#         print(x, sep=' ')