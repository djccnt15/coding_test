n = int(input())
for i in range(1, n * 2):
    print('*' * i if i <= n else '*' * ((2 * n) - i))