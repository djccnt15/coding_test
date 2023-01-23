n = int(input())
[print('*' * i if i <= n else '*' * ((2 * n) - i)) for i in range(1, n * 2)]