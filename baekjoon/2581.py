def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


d = [v for v in (i for i in range(*[int(input()), int(input()) + 1])) if is_prime(v)]
print(sum(d), min(d), sep='\n') if d else print(-1)