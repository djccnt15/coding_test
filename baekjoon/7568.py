def comp(a, b):
    return True if a[0] < b[0] and a[1] < b[1] else False


n = int(input())
p = [[int(x) for x in input().split()] for _ in range(n)]
[print(x + 1, end=' ') for x in [(sum(comp(p[i], p[j]) for j in range(n) if i != j)) for i in range(n)]]


# p = [[int(x) for x in input().split()] for _ in range(int(input()))]
# for a in p:
#     r = 1
#     for b in p:
#         if p.index(a) != p.index(b):
#             if a[0] < b[0] and a[1] < b[1]: r += 1
#     print(r, end=' ')