import lp

def f(s):
  a = s.NumVar(0, s.infinity(), 'haw to rockingham (mgd)')
  b = s.NumVar(0, s.infinity(), 'deep to rockingham (mgd)')
  c = s.NumVar(0, s.infinity(), 'haw to guilford (mgd)')
  d = s.NumVar(0, s.infinity(), 'deep to guilford (mgd)')
  e = s.NumVar(0, s.infinity(), 'haw to standolf (mgd)')
  f = s.NumVar(0, s.infinity(), 'deep to standolf (mgd)')
  g = s.NumVar(0, s.infinity(), 'haw to alamance (mgd)')
  h = s.NumVar(0, s.infinity(), 'deep to alamance (mgd)')

  s.Minimize(3200*a + 2600*b + 7100*c + 4100*d + 6700*e + 3700*f + 4300*g + 2100*h)

  s.Add(a + b >= 3.6, 'rockingham demand (mgd)')
  s.Add(c + d >= 3.1, 'guilford demand (mgd)')
  s.Add(e + f >= 2.4, 'standolf demand (mgd)')
  s.Add(g + h >= 4.2, 'alamance demand (mgd)')
  s.Add(a + c + e + g <= 7.5, 'haw supply (mgd)')
  s.Add(b + d + f + h <= 6.1, 'deep supply (mgd)')

lp.analyze(f)
