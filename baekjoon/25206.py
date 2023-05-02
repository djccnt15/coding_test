# from dataclasses import dataclass


# @dataclass
# class Gp:
#     point: float
#     grade: str

#     def score(self):
#         return self.point * table[self.grade]


# table = {
#     'A+': 4.5,
#     'A0': 4.0,
#     'B+': 3.5,
#     'B0': 3.0,
#     'C+': 2.5,
#     'C0': 2.0,
#     'D+': 1.5,
#     'D0': 1.0,
#     'F': 0.0
# }

# array = []
# total = 0

# for _ in range(20):
#     _, p, g = input().split()
#     if g == 'P':
#         continue
#     else:
#         p = float(p)
#         total += p
#         array.append(Gp(p, g).score())

# print(sum(array) / total)


table = {
    'A+': 4.5,
    'A0': 4.0,
    'B+': 3.5,
    'B0': 3.0,
    'C+': 2.5,
    'C0': 2.0,
    'D+': 1.5,
    'D0': 1.0,
    'F': 0.0
}

score = total = 0

for _ in range(20):
    _, p, g = input().split()
    if g == 'P':
        continue
    else:
        p = float(p)
        total += p
        score += table[g] * p

print(score / total)