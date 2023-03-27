import sys

for _ in range(int(input())):
    print(sum(int(x) for x in sys.stdin.readline().split()))