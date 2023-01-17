def grp(a):
    return list(a) == sorted(a, key=a.find)


print(sum(grp(input()) for _ in range(int(input()))))