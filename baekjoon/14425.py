import sys
input = sys.stdin.readline
n, m = [int(x) for x in input().split()]
s = {input() for _ in range(n)}
m = [input() for _ in range(m)]
print(sum(1 for x in m if x in s))