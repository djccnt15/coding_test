import sys

input = sys.stdin.readline
s = []
cnt = 0

for _ in range(int(input())):
    i = input().split()
    if i[0] == 'pop':
        if len(s) > cnt:
            print(s[cnt])
            cnt += 1
        else:
            print(-1)
    elif i[0] == 'size':
        print(len(s) - cnt)
    elif i[0] == 'empty':
        print(1 if len(s) == cnt else 0)
    elif i[0] == 'front':
        print(s[cnt] if len(s) > cnt else -1)
    elif i[0] == 'back':
        print(s[-1] if len(s) > cnt else -1)
    else:
        s.append(i[-1])