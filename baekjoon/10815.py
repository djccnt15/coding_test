input()
n = {int(x) for x in input().split()}
input()
m = [int(x) for x in input().split()]
[print(1 if x in n else 0, end=' ') for x in m]