def r(n):
    if n == 1:
        return ["*"]

    s = r(n // 3)
    L = []

    for S in s:
        L.append(S * 3)
    for S in s:
        L.append(S + " " * (n // 3) + S)
    for S in s:
        L.append(S * 3)
    return L


n = int(input())
print("\n".join(r(n)))


# https://cotak.tistory.com/38