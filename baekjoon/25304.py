def mul(a, b):
    return a * b


print(
    'Yes' if int(input()) == sum(
        mul(*[int(x) for x in input().split()]) for _ in range(int(input()))
    )
    else 'No'
)