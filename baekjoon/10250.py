for _ in range(int(input())):
    h, w, n = [int(x) for x in input().split()]
    print(h * 100 + n // h if n % h == 0 else n % h * 100 + n // h + 1)