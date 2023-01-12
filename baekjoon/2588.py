a, b = [int(input()) for _ in range(2)]
print(b % 10 * a, b % 100 // 10 * a, b // 100 * a, a * b, sep='\n')