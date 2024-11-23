from analyze import analyze

import pulp

x = pulp.LpVariable.dicts("x", [1, 2], 0)

p = pulp.LpProblem("z", pulp.LpMaximize)

p += x[1] + x[2]

p += 6 * x[1] + 1 * x[2] <= 1
p += 5 * x[1] + 8 * x[2] <= 1

analyze(p)
