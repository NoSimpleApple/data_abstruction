#!/usr/bin/python3

# 占位高阶过程
_sm_proc = lambda obj: obj


class Fraction(object):

    def __init__(self, numer, denom):

        if denom == 0:
            raise ZeroDivisionError("value zero found on demon")

        elif numer == 0:
            self._is_negative_or_zero = 0

        elif numer * denom < 0:
            self._is_negative_or_zero = -1

        elif numer * denom > 0:
            self._is_negative_or_zero = 1

        find_approx_num = self._find_approx_num
        self._approx = find_approx_num(numer, denom)

        self._numer = self._is_negative_or_zero * abs(numer // self._approx)
        self._demon = abs(denom // self._approx)

    @staticmethod
    def _find_approx_num(x: int, y: int):
        if not x * y:
            return 1

        x, y = abs(x), abs(y)

        while x != y:
            if x < y:
                x, y = y, x
            x = x - y
        return x

    @classmethod
    def _crt_radio(cls):
        return cls.__new__(cls)

    def __add__(self, other):
        numer = self.numer * other.denom + self.denom * other.numer
        demon = self.denom * other.denom
        outcome = Fraction(numer, demon)

        return outcome

    def __sub__(self, other):
        numer = self.numer * other.denom - self.denom * other.numer
        demon = self.denom * other.denom
        outcome = Fraction(numer, demon)

        return outcome

    def __mul__(self, other):
        numer = self.numer * other.numer
        demon = self.denom * other.denom
        outcome = Fraction(numer, demon)

        return outcome

    def __lt__(self, other):
        return self.numer * other.denom > other.numer * self.denom

    def __le__(self, other):
        return not self.__gt__(other)

    def __gt__(self, other):
        return self.numer * other.denom < other.numer * self.denom

    def __ge__(self, other):
        return not self.__lt__(other)

    def __eq__(self, other):
        return all((
            self.numer == other.numer,
            self.denom == other.denom
        ))

    def __str__(self):
        return f'{self.numer}/{abs(self.denom)}'

    def __repr__(self):
        return f'{self.__class__} ' \
               f'(sign={self._is_negative_or_zero}, approximate={self._approx}) ' \
               f'src: {self._numer}/{self._demon} '

    @property
    def numer(self):
        return self._numer

    @property
    def denom(self):
        return self._demon
