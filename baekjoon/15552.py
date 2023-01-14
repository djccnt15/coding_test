import sys

[print(sum(int(x) for x in sys.stdin.readline().split())) for _ in range(int(input()))]