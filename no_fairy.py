import lp

import json
import math

def f(s):
  with open('no_fairy_chart.json') as f:
    multipliers = json.load(f)

  coefs = {}
  for att_type in multipliers:
    coefs[att_type] = {
      def_type: math.log2((multipliers[att_type][def_type] + .2)
                          / (multipliers[def_type][att_type] + .2))
      for def_type in multipliers
    }

  x = {type: s.NumVar(0, s.infinity(), type) for type in coefs}
  e = s.NumVar(-s.infinity(), s.infinity(), 'E')

  s.Maximize(e)

  s.Add(sum(x.values()) == 1)

  for opp_type in coefs:
    s.Add(
      sum(coefs[my_type][opp_type] * x[my_type] for my_type in coefs) >= e,
      f'opponent {opp_type}'
    )

lp.analyze(f)
