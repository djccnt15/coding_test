input()
n = {int(x) for x in input().split()}
input()
m = [int(x) for x in input().split()]
for x in m:
    print(1 if x in n else 0, end=' ')