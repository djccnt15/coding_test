while True:
    x = int(input())
    if x == -1:
        break
    else:
        a = [v for v in range(1, x) if x % v == 0]
        print(f"{x} = {' + '.join([str(y) for y in a])}" if sum(a) == x else f"{x} is NOT perfect.")