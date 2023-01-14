input()
d = [int(x) for x in input().split()]
print(sum(a / max(d) * 100 for a in d) / len(d))