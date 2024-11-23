from analyze import analyze


def f(s) -> None:
    a = s.NumVar(0, s.infinity(), "convenience")
    b = s.NumVar(0, s.infinity(), "standard")
    c = s.NumVar(0, s.infinity(), "expanded")

    s.Maximize(1.2 * a + 2 * b + 2.6 * c)

    s.Add(a + b + c <= 11, "stores")
    s.Add(4.125 * a + 8.25 * b + 12.375 * c <= 82.5, "capital (million $)")
    s.Add(30 * a + 15 * b + 45 * c <= 300, "employees")


analyze(f)
