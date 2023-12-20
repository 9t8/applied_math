from lp import analyze

import json
import math

with open('data/no_fairy.json') as file:
  multipliers = json.load(file)

coefs = {}
for att_type in multipliers:
  coefs[att_type] = {
    def_type: math.log2((multipliers[att_type][def_type] + .2)
                        / (multipliers[def_type][att_type] + .2))
    for def_type in multipliers
  }

def f(s):
  x = {type: s.NumVar(0, s.infinity(), type) for type in coefs}
  e = s.NumVar(-s.infinity(), s.infinity(), 'E')

  s.Maximize(e)

  s.Add(sum(x.values()) == 1, 'probabilities')

  for opp_type in coefs:
    s.Add(
      sum(coefs[my_type][opp_type] * x[my_type] for my_type in coefs) >= e,
      f'opponent {opp_type}'
    )

analyze(f)
