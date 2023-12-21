from analyze import analyze

import pulp

x = pulp.LpVariable.dicts('x', [1, 2], 0)

p = pulp.LpProblem('z', pulp.LpMinimize)

p += sum(x.values())

shift = 42

p += (-41.5781+shift)*x[1] + (30.982+shift)*x[2] >= 1
p += (7.942+shift)*x[1] + (-5.918+shift)*x[2] >= 1

analyze(p)

print(1/pulp.value(p.objective) - shift)
for e in x.values():
  print(pulp.value(e)/pulp.value(p.objective))
