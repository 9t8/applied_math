import highspy

h = highspy.Highs()
inf = highspy.kHighsInf

c = (1, 1)
for i in range(len(c)):
  h.addVar(0, inf)
  h.changeColCost(i, c[i])

for A_i, b_i in (
  ((6, 1), 1),
  ((5, 8), 1)
):
  h.addRow(b_i, inf, len(A_i), (*range(len(A_i)),), A_i)

h.run()
print()
h.writeSolution('', 1)
