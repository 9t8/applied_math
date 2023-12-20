import pulp

def analyze(p):
  p.solve()

  print(f'Status: {pulp.LpStatus[p.status]}')
  print(f'{p.name} = {pulp.value(p.objective)}')

  print('Variables')
  print(f'{"Name":16} {"Value":>12} {"Reduced cost":>12} {"Coefficient":>12}')
  for v in p.variables():
      print(f'{v.name:16.16} {pulp.value(v):12} {v.dj:12} {p.objective.get(v, 0):12}')

  print('Constraints')
  print(f'{"Name":16} {"Value":>12} {"Shadow price":>12} {"Bound":>12}')
  for c in p.constraints.values():
    print(f'{c.name:16.16} {-c.constant - c.slack:12} {c.pi:12} {-c.constant:12}')
