from analyze import analyze


def f(s) -> None:
    a = s.NumVar(0, s.infinity(), "skimboards")
    b = s.NumVar(0, s.infinity(), "skateboards")

    s.Maximize(50 * a + 30 * b)

    s.Add(1 / 4 * a + 1 / 8 * b <= 35, "plywood (sheets)")
    s.Add(2 / 3 * a + 1 / 2 * b <= 120, "saw time (hours)")
    s.Add(a <= 100, "resin (skimboards)")
    s.Add(2 * b <= 400, "sanding (hours)")


analyze(f)
