import lp

def f(s):
  a = s.NumVar(0, s.infinity(), 'maize flour (g)')
  b = s.NumVar(0, s.infinity(), 'tangerines (g)')
  c = s.NumVar(0, s.infinity(), 'pigeon peas (g)')
  d = s.NumVar(0, s.infinity(), 'matemba (g)')
  e = s.NumVar(0, s.infinity(), 'potatoes (g)')
  f = s.NumVar(0, s.infinity(), 'Chinese cabbage (g)')

  ec = [3.620, .532, 1.190, .956, .931, .131] # energy content (Cal/g)

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

  s.Add(1000 <= ec[0]*a, 'min maize flour (Cal)')
  s.Add(ec[0]*a <= 1200, 'max maize flour (Cal)')
  s.Add(50 <= ec[1]*b, 'min tangerines (Cal)')
  s.Add(ec[1]*b <= 100, 'max tangerines (Cal)')
  s.Add(100 <= ec[2]*c, 'min pigeon peas (Cal)')
  s.Add(ec[2]*c <= 250, 'max pigeon peas (Cal)')
  s.Add(100 <= ec[3]*d, 'min matemba (Cal)')
  s.Add(ec[3]*d <= 300, 'max matemba (Cal)')
  s.Add(80 <= ec[4]*e, 'min potatoes (Cal)')
  s.Add(ec[4]*e <= 160, 'max potatoes (Cal)')
  s.Add(15 <= ec[5]*f, 'min Chinese cabbage (Cal)')
  s.Add(ec[5]*f <= 30, 'max Chinese cabbage (Cal)')

lp.analyze(f)
