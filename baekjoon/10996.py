n = int(input())
for _ in range(1, n + 1):
    if n % 2 == 1:
        print('* ' * (n - n // 2), ' *' * (n // 2), sep='\n')
    else:
        print('* ' * (n // 2), ' *' * (n - n // 2), sep='\n')