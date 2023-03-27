n = int(input())
for i in range(1, n * 2):
    print(
        ' '*(i - 1) + '*' * ((n - i) * 2 + 1) if i <= n
        else ' ' * (n * 2 - i - 1) + '*' * ((i - n) * 2 + 1)
    )