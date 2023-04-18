i = int(input())
for j in range(i * 2 - 1):
    if j < i:
        print(' ' * (i - (j + 1)) + '*' * (j * 2 + 1))
    else:
        print(' ' * (j + 1 - i) + '*' * (((i * 2 - 1) - j) * 2 - 1))


# i = int(input())
# j = list(zip([i for i in range(i)][::-1], [i * 2 + 1 for i in range(i)]))
# k = [j[a] if a < i else j[i - a - 2] if i - a - 2 >= -i else 0 for a in range(i * 2)][:-1]
# for v in k:
#     print((' ' * v[0]) + ('*' * v[1]))