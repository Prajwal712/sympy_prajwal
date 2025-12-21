from sympy import symbols, cos, sin, solve, I, log
from sympy.testing.pytest import raises

def test_issue_28804():
    # Define the 2-link arm kinematics symbols
    a, b, x, y, l1, l2 = symbols('a b x y l1 l2')

    eqs = [
        l1*cos(a) + l2*cos(a+b) - x,
        l1*sin(a) + l2*sin(a+b) - y
    ]

    # This used to crash with TypeError or hang
    sol = solve(eqs, [a, b])

    # We just want to assert that we got a solution (list is not empty)
    assert len(sol) > 0

    # Optional: Check that the result contains log/I (indicating it used the exp rewrite)
    assert any(s[0].has(log) or s[0].has(I) for s in sol)
