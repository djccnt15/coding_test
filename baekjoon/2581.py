def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


d = [v for v in (i for i in range(*[int(input()), int(input()) + 1])) if is_prime(v) is True]
print(-1) if bool(d) is False else print(sum(d), min(d), sep='\n')
# print(-1 if bool(d) is False else sum(d), min(d), sep='\n')  # runtime error