#!/usr/bin/python3

# 占位高阶过程
_sm_proc = lambda obj: obj


class Ratio(object):

    def __init__(self, numer, demon):

        find_approx_num = self._find_approx_num

        self._approx = find_approx_num(numer, demon)

        if demon == 0:
            raise ZeroDivisionError("value zero found on demon")

        elif numer == 0:
            self._is_negative_or_zero = 0

        elif numer * demon < 0:
            self._is_negative_or_zero = -1

        elif numer * demon > 0:
            self._is_negative_or_zero = 1

        # debug
        self._approx = 1
        #

        self._numer = self._is_negative_or_zero * abs(numer // self._approx)
        self._demon = abs(demon // self._approx)

    @staticmethod
    def _find_approx_num(x: int, y: int):
        x = abs(x)
        y = abs(y)

        n = max(x, y)
        m = min(x, y)

        while n == m:
            n = max(n, m)
            a = n - m
            m = min(n, m, a)

        return m

    @classmethod
    def _crt_radio(cls):
        return cls.__new__(cls)

    def __add__(self, other):
        numer = self.numer * other.demon + self.demon * other.numer
        demon = self.demon * other.demon
        outcome = Ratio(numer, demon)

        return outcome

    def __sub__(self, other):
        numer = self.numer * other.demon - self.demon * other.numer
        demon = self.demon * other.demon
        outcome = Ratio(numer, demon)

        return outcome

    def __mul__(self, other):
        numer = self.numer * other.numer
        demon = self.demon * other.demon
        outcome = Ratio(numer, demon)

        return outcome

    def __divmod__(self, other):
        pass

    def __lt__(self, other):
        return self.numer * other.demon > other.numer * self.demon

    def __le__(self, other):
        return not self.__gt__(other)

    def __gt__(self, other):
        return self.numer * other.demon < other.numer * self.demon

    def __ge__(self, other):
        return not self.__lt__(other)

    def __eq__(self, other):
        return all((
            self.numer == other.numer,
            self.demon == other.demon
        ))

    def __str__(self):
        return f"{self.numer}/{abs(self.demon)}"

    @property
    def numer(self):
        return self._numer

    @property
    def demon(self):
        return self._demon
