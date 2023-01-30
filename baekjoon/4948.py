def prime(m):
    n = m * 2
    d = [i for i in range(2, n + 1)]
    c = {j for i in range(2, int(n ** 0.5) + 1) for j in range(i * 2, n + i, i)}
    print(len([v for v in d if v > m and v not in c]))


while 1:
    m = int(input())
    if m != 0:
        prime(m)
    else:
        break


# def is_prime(n):
#     if n == 1:
#         return False
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return True


# while 1:
#     m = int(input())
#     if m != 0:
#         print(sum(is_prime(m) for m in range(m + 1, m * 2 + 1)))
#     else:
#         break