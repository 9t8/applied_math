import lp

def f(s):
  ec = [3.620, .532, 1.190, .956, .931, .131] # energy content (Cal/g)

  a = s.NumVar(1000/ec[0], 1200/ec[0], 'maize flour (g)')
  b = s.NumVar(50/ec[1], 100/ec[1], 'tangerines (g)')
  c = s.NumVar(100/ec[2], 250/ec[2], 'pigeon peas (g)')
  d = s.NumVar(100/ec[3], 300/ec[3], 'matemba (g)')
  e = s.NumVar(80/ec[4], 160/ec[4], 'potatoes (g)')
  f = s.NumVar(15/ec[5], 30/ec[5], 'Chinese cabbage (g)')

  s.Minimize(ec[0]*a + ec[1]*b + ec[2]*c + ec[3]*d + ec[4]*e + ec[5]*f)

  # nutritional data
  nutritional_data = [
    [.08120, .00805, .06760, .20100, .01960, .01500, 'protein (g)', 20],
    [.0612, .3640, .4290, .1000, .0507, 1.0500, 'Ca (mg)', 400],
    [.03450, .00156, .10000, .00556, .00350, .00800, 'Fe (mg)', 7],
    [.2450, .1560, 1.1000, .2440, .0922, .6630, 'vitamin B9 (mcg)', 50],
    [0, 0, 0, .0158, 0, 0, 'vitamin B12 (mcg)', .5],
    [0, .268, 0, 0, .128, .450, 'vitamin C (mg)', 20],
    [.00385, .00058, .00148, .00041, .00105, .00040, 'vitamin B1 (mg)', .7],
    [.00201, .00036, .00571, .00063, .00021, .00070, 'vitamin B2 (mg)', 1.1],
    [.03630, .00377, .00781, .03900, .01390, .00500, 'vitamin B3 (mg)', 12.1],
    [.112, .338, 0, 0, 0, 2.230, 'vitamin A (mcg)', 400]
  ]

  for nd in nutritional_data:
    s.Add(nd[0]*a + nd[1]*b + nd[2]*c + nd[3]*d + nd[4]*e + nd[5]*f >= nd[7], nd[6])

lp.analyze(f)
