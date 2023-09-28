from ortools.linear_solver import pywraplp

def analyze(f, solver_id='GLOP'):
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
  print(f'Objective value: {o.Value()}')

  print('Variables')
  print(f'{"Value":>12} {"Reduced cost":>12} {"Coefficient":>12} Name')
  for var in s.variables():
    print(f'{var.solution_value():12.6} {var.reduced_cost():12.6} {o.GetCoefficient(var):12.6} {var}')

  print('Constraints')
  print(f'{"Value":>12} {"Shadow price":>12} {"Bound":>12} Name')
  for cons, val in zip(s.constraints(), s.ComputeConstraintActivities()):
    finite = lambda x : -pywraplp.Solver.infinity() < x < pywraplp.Solver.infinity()
    if finite(cons.lb()):
      bound = 'TWO BOUNDS' if finite(cons.ub()) else cons.lb()
    else:
      bound = cons.ub() if finite(cons.ub()) else 'NO BOUNDS'

    print(f'{val:12.6} {cons.dual_value():12.6} {bound:>12} {cons.name()}')
