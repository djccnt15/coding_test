m = [int(x) for x in (input() for _ in range(5))]
print(min(m[:3]) + min(m[3:]) - 50)