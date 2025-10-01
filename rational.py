from math import gcd

class Rational:
    def __init__(self, p: int, q: int):
        if q == 0:
            raise ZeroDivisionError("Denominator cannot be zero")
        
        # normalize sign: denominator always positive
        if q < 0:
            p, q = -p, -q
        
        # reduce fraction
        g = gcd(p, q)
        self.p = p // g
        self.q = q // g

    def __eq__(self, other):
        if not isinstance(other, Rational):
            return NotImplemented
        return self.p == other.p and self.q == other.q

    def __add__(self, other):
        if not isinstance(other, Rational):
            return NotImplemented
        num = self.p * other.q + other.p * self.q
        den = self.q * other.q
        return Rational(num, den)

    def __mul__(self, other):
        if not isinstance(other, Rational):
            return NotImplemented
        num = self.p * other.p
        den = self.q * other.q
        return Rational(num, den)

    def __neg__(self):
        return Rational(-self.p, self.q)

    def __repr__(self):
        return f"{self.p}/{self.q}"
    
    def to_float(self):
        return self.p / self.q
