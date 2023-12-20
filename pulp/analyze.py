import pulp

def analyze(p):
  p.solve()

  print(f'Status: {pulp.LpStatus[p.status]}')
  print(f'{p.name} = {pulp.value(p.objective)}')

  print('Variables')
  print(f'{"Value":>12} {"Reduced cost":>12} {"Coefficient":>12} Name')
  for v in p.variables():
      print(f'{pulp.value(v):12} {v.dj:12.6} {p.objective.get(v, 0):12} {v}')

  print('Constraints')
  print(f'{"Value":>12} {"Shadow price":>12} {"Bound":>12} Name')
  for c in p.constraints.values():
    print(f'{-c.constant - c.slack:12.6} {c.pi:12} {-c.constant:12} {c.name}')
