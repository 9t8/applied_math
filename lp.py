import math

from ortools.linear_solver import pywraplp

def analyze(f):
  s = pywraplp.Solver.CreateSolver('GLOP')
  assert s

  f(s)

  status = s.Solve()

  if status != s.OPTIMAL:
    print('No optimal solution!')

  o = s.Objective()
  print(f'Objective value: {o.Value()}')

  print(f'\n{"Value":12}  {"Reduced cost":12}  {"Obj. coef.":12}  Variable name')
  for var in s.variables():
    print(f'{var.solution_value():12.6}  {var.reduced_cost():12.6}  {o.GetCoefficient(var):12.6}  {var}')

  print(f'\n{"Value":12}  {"Shadow price":12}  {"Bound":12}  Constraint name')
  for cons, val in zip(s.constraints(), s.ComputeConstraintActivities()):
    if cons.lb() != -math.inf:
      bound = cons.lb() if cons.ub() == math.inf else 'TWO BOUNDS'
    else:
      bound = cons.ub() if cons.ub() != math.inf else 'NO BOUNDS'

    print(f'{val:12.6}  {cons.dual_value():12.6}  {bound:12}  {cons.name()}')
