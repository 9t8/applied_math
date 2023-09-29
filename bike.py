import highspy

h = highspy.Highs()
inf = highspy.kHighsInf

h.changeObjectiveSense(highspy.ObjSense.kMaximize)

c = (180, 120, 220)
for i in range(len(c)):
  h.addVar(0, inf)
  h.changeColCost(i, c[i])

for A_i, b_i in (
  ((17, 17, 34), 85000),
  ((12, 21, 15), 42000)
):
  h.addRow(-inf, b_i, len(A_i), (*range(len(A_i)),), A_i)

h.run()
print()
h.writeSolution('', 1)
# https://github.com/ERGO-Code/HiGHS/blob/v1.5.4/src/lp_data/HConst.h#L138-L147
# 1 and 3 are useful
