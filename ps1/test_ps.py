import ps1a, ps1b, ps1c


def test_ps1a():
    assert ps1a.get_months(120000, .10, 1000000) == 183
    assert ps1a.get_months(80000, .15, 500000) == 105


def test_ps1b():
    assert ps1b.get_months(120000, .05, 500000, .03) == 142
    assert ps1b.get_months(80000, .1, 800000, .03) == 159
    assert ps1b.get_months(75000, .05, 1500000, .05) == 261


def test_ps1c():
    assert ps1c.get_savings_rate(150000) == ("0.4411", 12)
    assert ps1c.get_savings_rate(300000) == ("0.2205", 13)
    assert ps1c.get_savings_rate(10000)[0] == "It is not possible to pay the down payment in three years."