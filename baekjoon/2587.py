d = [int(x) for x in [input() for _ in range(5)]]
print(int(sum(d) / len(d)), sorted(d)[2], sep='\n')