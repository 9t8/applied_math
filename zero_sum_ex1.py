import lp

def f(s):
  p1 = s.NumVar(0, s.infinity(), 'P1')
  p2 = s.NumVar(0, s.infinity(), 'P2')
  e = s.NumVar(0, s.infinity(), 'E')

  s.Maximize(e)

  s.Add(p1 + p2 == 1)
  s.Add(5*p1 + 0*p2 >= e)
  s.Add(4*p1 + 7*p2 >= e)

lp.analyze(f)
