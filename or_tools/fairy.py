import math

import pandas as pd
from analyze import analyze

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


def f(s) -> None:
    e = s.NumVar(-s.infinity(), s.infinity(), "E")
    x = {type: s.NumVar(0, s.infinity(), type) for type in coefs}

    s.Maximize(e)

    s.Add(sum(x.values()) == 1, "probabilities")

    for opp_type in coefs:
        s.Add(
            sum(coefs[my_type][opp_type] * x[my_type] for my_type in coefs) >= e,
            f"opponent {opp_type}",
        )

    s.EnableOutput()


analyze(f)
