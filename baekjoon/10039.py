s = [x if x > 40 else 40 for x in (int(x) for x in (input() for _ in range(5)))]
print(sum(s) // len(s))