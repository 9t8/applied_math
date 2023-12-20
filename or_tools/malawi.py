from analyze import analyze

def f(s):
  x = (
    s.NumVar(0, s.infinity(), 'maize flour (g)'),
    s.NumVar(0, s.infinity(), 'tangerines (g)'),
    s.NumVar(0, s.infinity(), 'pigeon peas (g)'),
    s.NumVar(0, s.infinity(), 'chicken (g)'),
    s.NumVar(0, s.infinity(), 'potatoes (g)'),
    s.NumVar(0, s.infinity(), 'Chinese cabbage (g)')
  )

  c = (3.620, .532, 1.190, 2.15, .931, .131) # energy content (Cal/g)

  s.Minimize(sum(a*b for a, b in zip(c, x)))

  # nutritional constraints
  for A_i, b_i, name in (
    ((.08120, .00805, .06760, .2400, .01960, .01500), 20, 'protein (g)'),
    (( .0612,  .3640,  .4290, .1500,  .0507, 1.0500), 400, 'Ca (mg)'),
    ((.03450, .00156, .10000, .0130, .00350, .00800), 7, 'Fe (mg)'),
    (( .2450,  .1560, 1.1000, .0400,  .0922,  .6630), 50, 'vitamin B9 (mcg)'),
    ((     0,      0,      0, .0034,      0,      0), .5, 'vitamin B12 (mcg)'),
    ((     0,   .268,      0, .0000,   .128,   .450), 20, 'vitamin C (mg)'),
    ((.00385, .00058, .00148, .0007, .00105, .00040), .7, 'vitamin B1 (mg)'),
    ((.00201, .00036, .00571, .0012, .00021, .00070), 1.1, 'vitamin B2 (mg)'),
    ((.03630, .00377, .00781, .1371, .01390, .00500), 12.1, 'vitamin B3 (mg)'),
    ((  .112,   .338,      0, .0600,      0,  2.230), 400, 'vitamin A (mcg)')
  ):
    s.Add(sum(a*b for a, b in zip(A_i, x)) >= b_i, name)

  # Calorie constraints
  s.Add(1000 <= c[0]*x[0], 'min maize flour (Cal)')
  s.Add(c[0]*x[0] <= 1200, 'max maize flour (Cal)')
  s.Add(50 <= c[1]*x[1], 'min tangerines (Cal)')
  s.Add(c[1]*x[1] <= 100, 'max tangerines (Cal)')
  s.Add(100 <= c[2]*x[2], 'min pigeon peas (Cal)')
  s.Add(c[2]*x[2] <= 250, 'max pigeon peas (Cal)')
  s.Add(100 <= c[3]*x[3], 'min chicken (Cal)')
  # s.Add(ec[3]*x[3] <= 300, 'max chicken (Cal)')
  s.Add(80 <= c[4]*x[4], 'min potatoes (Cal)')
  s.Add(c[4]*x[4] <= 160, 'max potatoes (Cal)')
  s.Add(15 <= c[5]*x[5], 'min Chinese cabbage (Cal)')
  s.Add(c[5]*x[5] <= 30, 'max Chinese cabbage (Cal)')

analyze(f)
