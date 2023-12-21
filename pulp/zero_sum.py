from analyze import analyze

import pulp

x = pulp.LpVariable.dicts('x', [1, 2], 0)

p = pulp.LpProblem('z', pulp.LpMinimize)

p += sum(x.values())

shift = 10000

p += sum(a*b for a, b in zip((-41.5781+shift, 30.982+shift), x.values())) >= 1
p += sum(a*b for a, b in zip((7.942+shift, -5.918+shift), x.values())) >= 1

analyze(p)

print(1/(pulp.value(p.objective) or 0) - shift)
for e in x.values():
  print(pulp.value(e)/pulp.value(p.objective))
