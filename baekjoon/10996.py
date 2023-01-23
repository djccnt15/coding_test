n = int(input())
[
    print('* ' * (n - n // 2), ' *' * (n // 2), sep='\n') if n % 2 == 1
    else print('* ' * (n // 2), ' *' * (n - n // 2), sep='\n')
    for _ in range(1, n + 1)
]