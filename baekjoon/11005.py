import string

char = string.digits + string.ascii_uppercase


def convert(num: int, base: int) -> str:
    res = []
    while num:
        num, r = divmod(num, base)
        res.append(char[r])
    return ''.join(res[::-1])


n, b = [int(x) for x in input().split()]
print(convert(n, b))