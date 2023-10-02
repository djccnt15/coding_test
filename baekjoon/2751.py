import sys

input = sys.stdin.readline

for x in sorted([int(x) for x in [int(input()) for _ in range(int(input()))]]):
    print(x)