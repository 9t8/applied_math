import math

import pandas as pd
from analyze import analyze

import pulp

with open("data/fairy.csv") as file:
    df = pd.read_csv(file)

types = (*(t for t in df if t != "Attacking"),)

coefs = {}
for att_type in types:
    coefs[att_type] = {
        def_type: math.log2(
            (df[df["Attacking"] == att_type][def_type].iat[0] + 0.2)
            / (df[df["Attacking"] == def_type][att_type].iat[0] + 0.2)
        )
        for def_type in types
    }

e = pulp.LpVariable("E")
x = {type: pulp.LpVariable(type, 0) for type in coefs}

p = pulp.LpProblem("E", pulp.LpMaximize)

p += e

p += sum(x.values()) == 1, "probabilities"

for opp_type in coefs:
    p += (
        sum(coefs[my_type][opp_type] * x[my_type] for my_type in coefs) >= e,
        f"opponent {opp_type}",
    )

analyze(p)
