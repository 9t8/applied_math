def twelve_balls(b):
  # power = 3 ^ 3 = 27; possibilities = 2 * 12 = 24
  # By pigeonhole, power < possibilities --> we have lost.
  res1 = sum(b[0:4]) - sum(b[4:8])

  if res1 == 0: # power = 9; possibilities = 8
    res2 = sum(b[0:3]) - sum(b[8:11])

    if res2 == 0: # power = 3; possibilities = 2
      res3 = b[0] - b[11]
      if res3 < 0:
        return 11, 'heavier'
      assert res3 > 0
      return 11, 'lighter'

    res3 = b[8] - b[9]

    if res2 < 0: # power = 3; possibilities = 3
      if res3 == 0:
        return 10, 'heavier'
      if res3 < 0:
        return 9, 'heavier'
      assert res3 > 0
      return 8, 'heavier'

    assert res2 > 0 # power = 3; possibilities = 3
    if res3 == 0:
      return 10, 'lighter'
    if res3 < 0:
      return 8, 'lighter'
    assert res3 > 0
    return 9, 'lighter'

  res2 = b[0] + b[4] + b[8] - b[1] - b[2] - b[5]

  if res1 < 0: # power = 9; possibilities = 8
    if res2 == 0: # power = 3; possibilities = 3
      res3 = b[6] - b[7]
      if res3 == 0:
        return 3, 'lighter'
      if res3 < 0:
        return 7, 'heavier'
      assert res3 > 0
      return 6, 'heavier'
    elif res2 < 0: # power = 3; possibilities =
      pass
    elif res2 > 0: # power = 3; possibilities =
      pass

  assert res1 > 0 # power = 9; possibilities = 8
  if res2 == 0: # power = 3; possibilities = 3
    res3 = b[6] - b[7]
    if res3 == 0:
      return 3, 'heavier'
    if res3 < 0:
      return 6, 'lighter'
    assert res3 > 0
    return 7, 'lighter'
  elif res2 < 0: # power = 3; possibilities =
    pass
  elif res2 > 0: # power = 3; possibilities =
    pass
