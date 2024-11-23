from analyze import analyze

import pulp

x = pulp.LpVariable.dicts("x", [1, 2, 3], 0)

p = pulp.LpProblem("z", pulp.LpMaximize)

p += 180 * x[1] + 120 * x[2] + 220 * x[3]

p += 17 * x[1] + 17 * x[2] + 34 * x[3] <= 85000
p += 12 * x[1] + 21 * x[2] + 15 * x[3] <= 42000

analyze(p)
