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
  print(f'Objective = {o.Value()}')

  print('Variables')
  print(f'{"Name":16} {"Value":>12} {"Reduced cost":>12} {"Coefficient":>12}')
  for var in s.variables():
    print(f'{var.name():16.16} {var.solution_value():12.6} {var.reduced_cost():12.6} {o.GetCoefficient(var):12.6}')

  print('Constraints')
  print(f'{"Name":16} {"Value":>12} {"Shadow price":>12} {"Lower bound":>12} {"Upper bound":>12}')
  for cons, val in zip(s.constraints(), s.ComputeConstraintActivities()):
    print(f'{cons.name():16.16} {val:12.6} {cons.dual_value():12.6} {cons.lb():>12} {cons.ub():>12}')
