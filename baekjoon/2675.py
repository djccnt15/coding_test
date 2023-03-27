for _ in range(int(input())):
    a, b = input().split()
    print(''.join(v * int(a) for v in b))