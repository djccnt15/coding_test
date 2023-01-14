h, m, t = [int(x) for _ in range(2) for x in input().split()]
print((h + ((m + t) // 60)) % 24, (m + t) % 60)