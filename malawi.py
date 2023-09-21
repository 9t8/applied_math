import lp

def f(s):
  x = (
    s.NumVar(0, s.infinity(), 'maize flour (g)'),
    s.NumVar(0, s.infinity(), 'tangerines (g)'),
    s.NumVar(0, s.infinity(), 'pigeon peas (g)'),
    s.NumVar(0, s.infinity(), 'matemba (g)'),
    s.NumVar(0, s.infinity(), 'potatoes (g)'),
    s.NumVar(0, s.infinity(), 'Chinese cabbage (g)')
  )

  ec = (3.620, .532, 1.190, .956, .931, .131) # energy content (Cal/g)

  s.Minimize(sum(a*b for a, b in zip(ec, x)))

  nutritional_data = (
    ((.08120, .00805, .06760, .20100, .01960, .01500), 20, 'protein (g)'),
    ((.0612, .3640, .4290, .1000, .0507, 1.0500), 400, 'Ca (mg)'),
    ((.03450, .00156, .10000, .00556, .00350, .00800), 7, 'Fe (mg)'),
    ((.2450, .1560, 1.1000, .2440, .0922, .6630), 50, 'vitamin B9 (mcg)'),
    ((0, 0, 0, .0158, 0, 0), .5, 'vitamin B12 (mcg)'),
    ((0, .268, 0, 0, .128, .450), 20, 'vitamin C (mg)'),
    ((.00385, .00058, .00148, .00041, .00105, .00040), .7, 'vitamin B1 (mg)'),
    ((.00201, .00036, .00571, .00063, .00021, .00070), 1.1, 'vitamin B2 (mg)'),
    ((.03630, .00377, .00781, .03900, .01390, .00500), 12.1, 'vitamin B3 (mg)'),
    ((.112, .338, 0, 0, 0, 2.230), 400, 'vitamin A (mcg)')
  )

  for coeffs, bound, name in nutritional_data:
    s.Add(sum(a*b for a, b in zip(coeffs, x)) >= bound, name)

  s.Add(1000 <= ec[0]*x[0], 'min maize flour (Cal)')
  s.Add(ec[0]*x[0] <= 1200, 'max maize flour (Cal)')
  s.Add(50 <= ec[1]*x[1], 'min tangerines (Cal)')
  s.Add(ec[1]*x[1] <= 100, 'max tangerines (Cal)')
  s.Add(100 <= ec[2]*x[2], 'min pigeon peas (Cal)')
  s.Add(ec[2]*x[2] <= 250, 'max pigeon peas (Cal)')
  s.Add(100 <= ec[3]*x[3], 'min matemba (Cal)')
  s.Add(ec[3]*x[3] <= 300, 'max matemba (Cal)')
  s.Add(80 <= ec[4]*x[4], 'min potatoes (Cal)')
  s.Add(ec[4]*x[4] <= 160, 'max potatoes (Cal)')
  s.Add(15 <= ec[5]*x[5], 'min Chinese cabbage (Cal)')
  s.Add(ec[5]*x[5] <= 30, 'max Chinese cabbage (Cal)')

lp.analyze(f)
