def sf(n):
    return n + sum(int(x) for x in str(n))


s = {sf(i) for i in range(10001)}
[print(v) for v in range(10001) if v not in s]