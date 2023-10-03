import sys

input = sys.stdin.readline
s = []

for _ in range(int(input())):
    i = input().split()
    if i[0] == '1':
        s.append(i[-1])
    elif i[0] == '2':
        print(s.pop() if s else -1)
    elif i[0] == '3':
        print(len(s))
    elif i[0] == '4':
        print(1 if not s else 0)
    elif i[0] == '5':
        print(s[-1] if s else -1)