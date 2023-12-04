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

p.solve()

print(f'Status: {pulp.LpStatus[p.status]}')
print(f'{p.name} = {pulp.value(p.objective)}')

print('Variables')
print(f'{"Name":16} {"Value":>12} {"Reduced cost":>12} {"Coefficient":>12}')
for v in p.variables():
    print(f'{v.name:16.16} {pulp.value(v):12} {v.dj:12.6} {p.objective[v]:12}')

print('Constraints')
print(f'{"Name":16} {"Value":>12} {"Shadow price":>12} {"Bound":>12}')
for c in p.constraints.values():
  print(f'{c.name:16.16} {-c.constant - c.slack:12.6} {c.pi:12} {-c.constant:12}')

def f(s):
  a = s.NumVar(0, s.infinity(), 'skimboards')
  b = s.NumVar(0, s.infinity(), 'skateboards')

  s.Maximize(50*a + 30*b)

  s.Add(1/4*a + 1/8*b <= 35, 'plywood (sheets)')
  s.Add(2/3*a + 1/2*b <= 120, 'saw time (hours)')
  s.Add(a <= 100, 'resin (skimboards)')
  s.Add(2*b <= 400, 'sanding (hours)')

lp.analyze(f)
