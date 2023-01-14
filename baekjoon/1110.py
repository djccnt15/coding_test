c = 0
n = inp = int(input())
while 1:
    s = n // 10 + n % 10
    n = n % 10 * 10 + s % 10
    c += 1
    if n == inp: break
print(c)