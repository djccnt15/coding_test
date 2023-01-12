a, b, c = [int(x) for x in input().split()]
print((a + b) % c, (a % c + b % c) % c, (a * b) % c, (a % c * b % c) % c, sep='\n')