import pandas as pd
import pulp

import math

def pulp_analyze(p):
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

with open('data/fairy.csv') as file:
  df = pd.read_csv(file)

types = *(t for t in df if t != 'Attacking'),

coefs = {}
for att_type in types:
  coefs[att_type] = {
    def_type: math.log2((df[df['Attacking'] == att_type][def_type].iat[0] + .2)
                        / (df[df['Attacking'] == def_type][att_type].iat[0] + .2))
    for def_type in types
  }

x = {type: pulp.LpVariable(type, 0) for type in coefs}
e = pulp.LpVariable('E')

p = pulp.LpProblem('HELP', pulp.LpMaximize)
p += e

p += sum(x.values()) == 1, 'probabilities'

for opp_type in coefs:
  p += sum(coefs[my_type][opp_type] * x[my_type] for my_type in coefs) >= e, f'opponent {opp_type}'

pulp_analyze(p)
