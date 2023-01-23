l = [int(x) for x in input().split()]
print(
    'ascending' if l == [1, 2, 3, 4, 5, 6, 7, 8]
    else 'descending' if l == [8, 7, 6, 5, 4, 3, 2, 1]
    else 'mixed'
)