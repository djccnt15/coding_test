(n, m), l = ([int(x) for x in input().split()] for _ in range(2))
print(
    max(
        x for x in (
            l[a] + l[b] + l[c]
            for a in range(n - 2)
            for b in range(a + 1, n)
            for c in range(b + 1, n)
        ) if x <= m
    )
)


# from itertools import combinations

# (n, m), l = ([int(x) for x in input().split()] for _ in range(2))
# print(max(x for x in (sum(x) for x in list(combinations(l, 3))) if x <= m))