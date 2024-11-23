from analyze import analyze


def f(s) -> None:
    x = (
        s.NumVar(0, s.infinity(), "maize flour (g)"),
        s.NumVar(0, s.infinity(), "tangerines (g)"),
        s.NumVar(0, s.infinity(), "pigeon peas (g)"),
        s.NumVar(0, s.infinity(), "chicken (g)"),
        s.NumVar(0, s.infinity(), "potatoes (g)"),
        s.NumVar(0, s.infinity(), "Chinese cabbage (g)"),
    )

    c = (3.620, 0.532, 1.190, 2.15, 0.931, 0.131)  # energy content (Cal/g)

    s.Minimize(sum(a * b for a, b in zip(c, x)))

    # nutritional constraints
    for A_i, b_i, name in (
        ((0.08120, 0.00805, 0.06760, 0.2400, 0.01960, 0.01500), 20, "protein (g)"),
        ((0.0612, 0.3640, 0.4290, 0.1500, 0.0507, 1.0500), 400, "Ca (mg)"),
        ((0.03450, 0.00156, 0.10000, 0.0130, 0.00350, 0.00800), 7, "Fe (mg)"),
        ((0.2450, 0.1560, 1.1000, 0.0400, 0.0922, 0.6630), 50, "vitamin B9 (mcg)"),
        ((0, 0, 0, 0.0034, 0, 0), 0.5, "vitamin B12 (mcg)"),
        ((0, 0.268, 0, 0.0000, 0.128, 0.450), 20, "vitamin C (mg)"),
        ((0.00385, 0.00058, 0.00148, 0.0007, 0.00105, 0.00040), 0.7, "vitamin B1 (mg)"),
        ((0.00201, 0.00036, 0.00571, 0.0012, 0.00021, 0.00070), 1.1, "vitamin B2 (mg)"),
        (
            (0.03630, 0.00377, 0.00781, 0.1371, 0.01390, 0.00500),
            12.1,
            "vitamin B3 (mg)",
        ),
        ((0.112, 0.338, 0, 0.0600, 0, 2.230), 400, "vitamin A (mcg)"),
    ):
        s.Add(sum(a * b for a, b in zip(A_i, x)) >= b_i, name)

    # Calorie constraints
    s.Add(1000 <= c[0] * x[0], "min maize flour (Cal)")
    s.Add(c[0] * x[0] <= 1200, "max maize flour (Cal)")
    s.Add(50 <= c[1] * x[1], "min tangerines (Cal)")
    s.Add(c[1] * x[1] <= 100, "max tangerines (Cal)")
    s.Add(100 <= c[2] * x[2], "min pigeon peas (Cal)")
    s.Add(c[2] * x[2] <= 250, "max pigeon peas (Cal)")
    s.Add(100 <= c[3] * x[3], "min chicken (Cal)")
    # s.Add(ec[3]*x[3] <= 300, 'max chicken (Cal)')
    s.Add(80 <= c[4] * x[4], "min potatoes (Cal)")
    s.Add(c[4] * x[4] <= 160, "max potatoes (Cal)")
    s.Add(15 <= c[5] * x[5], "min Chinese cabbage (Cal)")
    s.Add(c[5] * x[5] <= 30, "max Chinese cabbage (Cal)")


analyze(f)
