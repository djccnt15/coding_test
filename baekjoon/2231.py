n = int(input())
a = [i for i in range(1, n + 1) if i + sum(int(x) for x in str(i)) == n]
print(a[0] if bool(a) is True else 0)


# n, a = int(input()), 0
# for i in range(1, n + 1):
#     if i + sum(int(x) for x in str(i)) == n:
#         a = i
#         break
# print(a)