import pandas as pd

with open('fairy_chart.csv') as t:
  d = pd.read_csv(t)
  print(d[d['Attacking'] == 'Normal']['Steel'])

types = *(t for t in d if t != 'Attacking'),
print(types)
