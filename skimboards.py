import pulp

import lp

p = pulp.LpProblem('Revenue', pulp.LpMaximize)

a = pulp.LpVariable('skimboards', 0)
b = pulp.LpVariable('skateboards', 0)

p += 50*a + 30*b

p += 1/4*a + 1/8*b <= 35, 'plywood_(sheets)'
p += 2/3*a + 1/2*b <= 120, 'saw time_(hours)'
p += a <= 100, 'resin_(skimboards)'
p += 2*b <= 400, 'sanding_(hours)'

lp.pulp_analyze(p)

def f(s):
  a = s.NumVar(0, s.infinity(), 'skimboards')
  b = s.NumVar(0, s.infinity(), 'skateboards')

  s.Maximize(50*a + 30*b)

  s.Add(1/4*a + 1/8*b <= 35, 'plywood (sheets)')
  s.Add(2/3*a + 1/2*b <= 120, 'saw time (hours)')
  s.Add(a <= 100, 'resin (skimboards)')
  s.Add(2*b <= 400, 'sanding (hours)')

lp.ortools_analyze(f)
