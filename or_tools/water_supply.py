from analyze import analyze


def f(s) -> None:
    a = s.NumVar(0, s.infinity(), "haw to rockingham")
    b = s.NumVar(0, s.infinity(), "haw to guilford")
    c = s.NumVar(0, s.infinity(), "haw to standolf")
    d = s.NumVar(0, s.infinity(), "haw to alamance")

    e = s.NumVar(0, s.infinity(), "deep to rockingham")
    f = s.NumVar(0, s.infinity(), "deep to guilford")
    g = s.NumVar(0, s.infinity(), "deep to standolf")
    h = s.NumVar(0, s.infinity(), "deep to alamance")

    s.Minimize(
        3200 * a
        + 7100 * b
        + 6700 * c
        + 4300 * d
        + 2600 * e
        + 4100 * f
        + 3700 * g
        + 2100 * h,
    )

    s.Add(a + b + c + d <= 7.5, "haw supply")
    s.Add(e + f + g + h <= 6.1, "deep supply")

    s.Add(a + e >= 3.6, "rockingham demand")
    s.Add(b + f >= 3.1, "guilford demand")
    s.Add(c + g >= 2.4, "standolf demand")
    s.Add(d + h >= 4.2, "alamance demand")


analyze(f)
