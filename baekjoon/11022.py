def res(i, a, b):
    print(f'Case #{i + 1}: {a} + {b} = {a + b}')

[res(i, *[int(x) for x in input().split()]) for i in range(int(input()))]