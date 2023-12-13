import lp

import pandas as pd

import math

with open('fairy_chart.csv') as t:
  df = pd.read_csv(t)

print(df.at[df['Attacking'] == 'Normal', 'Steel'])
types = *(t for t in df if t != 'Attacking'),
print(types)

# coefs = {}
# for att_type in types:
#   coefs[att_type] = {
#     def_type: math.log2((df[df['Attacking'] == att_type][def_type] + .2)
#                         / (df[df['Attacking'] == def_type][att_type] + .2))
#     for def_type in types
#   }
