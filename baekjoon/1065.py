def han(n):
    t = [int(v) for v in list(str(n))]
    return True if n < 100 and n > 0 \
        else True if len({t[i + 1] - t[i] for i in range(len(t) - 1)}) == 1 \
        else False


print(sum([han(i) for i in range(int(input()) + 1)]))