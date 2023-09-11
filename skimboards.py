from lp import analyze

def f(s):
  a = s.NumVar(0, s.infinity(), 'skimboards')
  b = s.NumVar(0, s.infinity(), 'skateboards')

  s.Add(1/4*a + 1/8*b <= 35, 'plywood')
  s.Add(2/3*a + 1/2*b <= 120, 'saw time')
  s.Add(a <= 100, 'resin')
  s.Add(2*b <= 400, 'sanding')

  s.Maximize(50*a + 30*b)

analyze(f)
