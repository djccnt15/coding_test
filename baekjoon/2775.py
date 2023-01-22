def test():
    a, b = int(input()), int(input()) + 1
    f = [[i for i in range(1, b)]]
    [f.append(list(sum(f[-1][:i]) for i in range(1, b))) for _ in range(a)]
    print(f[-1][-1])


[test() for _ in range(int(input()))]