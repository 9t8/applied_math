from analyze import analyze


def f(s) -> None:
    e = s.NumVar(0, s.infinity(), "E")
    p1 = s.NumVar(0, s.infinity(), "P1")
    p2 = s.NumVar(0, s.infinity(), "P2")

    s.Maximize(e)

    s.Add(p1 + p2 == 1)
    s.Add(6 * p1 + 1 * p2 >= e)
    s.Add(5 * p1 + 8 * p2 >= e)


analyze(f)
