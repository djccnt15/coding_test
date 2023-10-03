from collections import deque
import sys

input = sys.stdin.readline
d = deque()

for _ in range(int(input())):
    i = [int(i) for i in input().split()]
    if i[0] == 1:
        d.appendleft(i[-1])
    elif i[0] == 2:
        d.append(i[-1])
    elif i[0] == 3:
        print(d.popleft() if d else -1)
    elif i[0] == 4:
        print(d.pop() if d else -1)
    elif i[0] == 5:
        print(len(d))
    elif i[0] == 6:
        print(0 if d else 1)
    elif i[0] == 7:
        print(d[0] if d else -1)
    else:
        print(d[-1] if d else -1)