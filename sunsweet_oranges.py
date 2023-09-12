import lp

def f(s):
  a = s.NumVar(0, s.infinity(), 'ca to minneapolis')
  b = s.NumVar(0, s.infinity(), 'ca to indianapolis')
  c = s.NumVar(0, s.infinity(), 'ca to kansas city')
  d = s.NumVar(0, s.infinity(), 'ca to des moines')
  e = s.NumVar(0, s.infinity(), 'ca to omaha')
  f = s.NumVar(0, s.infinity(), 'ca to okc')
  g = s.NumVar(0, s.infinity(), 'fl to minneapolis')
  h = s.NumVar(0, s.infinity(), 'fl to indianapolis')
  i = s.NumVar(0, s.infinity(), 'fl to kansas city')
  j = s.NumVar(0, s.infinity(), 'fl to des moines')
  k = s.NumVar(0, s.infinity(), 'fl to omaha')
  l = s.NumVar(0, s.infinity(), 'fl to okc')

  s.Minimize(2701*a + 2906*b + 2216*c + 1861*d + 2176*e + 2360*f +
             2176*g + 1361*h + 1737*i + 1718*j + 1999*k + 1879*l)

  s.Add(a + b + c + d + e + f <= 180, 'ca supply')
  s.Add(g + h + i + j + k + l <= 80, 'fl supply')
  s.Add(a + g >= 66, 'minneapolis demand')
  s.Add(b + h >= 34, 'indianapolis demand')
  s.Add(c + i >= 42, 'kansas city demand')
  s.Add(d + j >= 15, 'des moines demand')
  s.Add(e + k >= 20, 'omaha demand')
  s.Add(f + l >= 30, 'okc demand')

lp.analyze(f)
