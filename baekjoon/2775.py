def test():
    a, b = int(input()), int(input())
    f = [[i for i in range(1, b + 1)]]
    [f.append(list(sum(f[-1][:i]) for i in range(1, b + 1))) for _ in range(a)]
    print(f[-1][-1])



[test() for _ in range(int(input()))]