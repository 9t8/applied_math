import pulp
from ortools.linear_solver import pywraplp

def pulp_analyze(p):
  p.solve()

  print(f'Status: {pulp.LpStatus[p.status]}')
  print(f'{p.name} = {pulp.value(p.objective)}')

  print('Variables')
  print(f'{"Value":>12} {"Reduced cost":>12} {"Coefficient":>12} Name')
  for v in p.variables():
      print(f'{pulp.value(v):12} {v.dj:12.6} {p.objective[v]:12} {v}')

  print('Constraints')
  print(f'{"Value":>12} {"Shadow price":>12} {"Bound":>12} Name')
  for c in p.constraints.values():
    print(f'{-c.constant - c.slack:12.6} {c.pi:12} {-c.constant:12} {c.name}')

def ortools_analyze(f, solver_id='GLOP'):
  s = pywraplp.Solver.CreateSolver(solver_id)
  if not s:
    print(f'Solver "{solver_id}" creation failed')
    return

  f(s)

  status = s.Solve()

  if status != s.OPTIMAL:
    print('No optimal solution')
    return

  o = s.Objective()
  print(f'Objective = {o.Value()}')

  print('Variables')
  print(f'{"Value":>12} {"Reduced cost":>12} {"Coefficient":>12} Name')
  for var in s.variables():
    print(f'{var.solution_value():12.6} {var.reduced_cost():12.6} {o.GetCoefficient(var):12.6} {var}')

  print('Constraints')
  print(f'{"Value":>12} {"Shadow price":>12} {"Bound":>12} Name')
  for val, cons in zip(s.ComputeConstraintActivities(), s.constraints()):
    finite = lambda x : -pywraplp.Solver.infinity() < x < pywraplp.Solver.infinity()
    if finite(cons.lb()):
      bound = 'TWO BOUNDS' if finite(cons.ub()) else cons.lb()
    else:
      bound = cons.ub() if finite(cons.ub()) else 'NO BOUNDS'

    print(f'{val:12.6} {cons.dual_value():12.6} {bound:>12} {cons.name()}')
