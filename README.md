# applied_math

[`fairy.csv` source](https://github.com/zonination/pokemon-chart)

[`no_fairy.json` source](https://gist.github.com/agarie/2620966)

[Print OR-Tools model:](https://github.com/google/or-tools/issues/520) `print(s.ExportModelAsLpFormat(False))`

PuLP is better for pure linear programming: CBC uses CLP, which is faster than GLOP. For other problems, CP-SAT is better than CBC.
