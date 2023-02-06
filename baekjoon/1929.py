m, n = (int(x) for x in (input().split()))
d = [i for i in range(2, n + 1)]
c = {j for i in range(2, int(n ** 0.5) + 1) for j in range(i * 2, n + i, i)}
[print(v) for v in d if v >= m and v not in c]


# def is_prime(n):
#     if n == 1:
#         return False
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return True


# a, b = (int(x) for x in (input().split()))
# [print(v) for v in (i for i in range(a, b + 1)) if is_prime(v)]