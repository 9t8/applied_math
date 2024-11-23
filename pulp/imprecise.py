from analyze import analyze

import pulp

x = pulp.LpVariable.dicts("x", [1, 2], 0)

p = pulp.LpProblem("z", pulp.LpMinimize)

p += sum(x.values())

shift = 42
# shift = 25000
C = ((-41.5781 + shift, 30.982 + shift), (7.942 + shift, -5.918 + shift))

# shift = 0
# C = (
#   (6000000+shift, 1000000+shift),
#   (5000000+shift, 8000000+shift)
# )

for row in C:
    p += sum(a * b for a, b in zip(row, x.values())) >= 1

analyze(p)

print(1 / (pulp.value(p.objective) or 0) - shift)
for e in x.values():
    print(pulp.value(e) / pulp.value(p.objective))
