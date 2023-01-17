def j():
    a, b = input().split()
    print(''.join([v * int(a) for v in b]))


[j() for _ in range(int(input()))]