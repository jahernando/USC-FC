from rational import Rational

from hypothesis import given, assume
import hypothesis.strategies as st

# Strategy: integers with non-zero denominator
rationals = st.tuples(st.integers(), st.integers().filter(lambda q: q != 0))

@given(rationals, rationals)
def test_commutativity_add(pair1, pair2):
    a, b = Rational(*pair1), Rational(*pair2)
    assert a + b == b + a

@given(rationals, rationals, rationals)
def test_associativity_mul(pair1, pair2, pair3):
    a, b, c = Rational(*pair1), Rational(*pair2), Rational(*pair3)
    assert (a * b) * c == a * (b * c)

@given(rationals)
def test_identity_add(pair):
    a = Rational(*pair)
    zero = Rational(0, 1)
    assert a + zero == a

@given(rationals)
def test_identity_mul(pair):
    a = Rational(*pair)
    one = Rational(1, 1)
    assert a * one == a
