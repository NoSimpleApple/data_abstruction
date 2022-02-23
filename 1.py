#!/usr/bin/python3

# 占位高阶过程
_sm_proc = lambda obj: obj


class Ratio(object):

    def __init__(self, numer, demon):

        find_approx_num = self._find_approx_num

        if isinstance(numer | demon, int):
            self._numer_proto = numer
            self._demon_proto = demon

            self._approx = find_approx_num(self._numer_proto,
                                           self._numer_proto
                                           )
            # debug #
            self._approx = 1
            #########

        else:
            raise SyntaxError("numer and demon must be type of int")

        self._numer = self._numer_proto // self._approx
        self._demon = self._demon_proto // self._approx

    @staticmethod
    def _find_approx_num(x: int, y: int):
        n = max(x, y)
        m = min(x, y)

        while n == m:
            n = max(n, m)
            a = n - m
            m = min(n, m, a)

        return m

    @classmethod
    def construct_radio(cls):
        return cls.__new__(cls)

    def __add__(self, other):
        outcome = other.construct_radio()
        outcome.__init__(self.numer * other.demon + self.demon * other.numer,
                         self.demon * other.demon
                         )

        return outcome.__str__()

    def __sub__(self, other):
        pass

    def __mul__(self, other):
        pass

    def __divmod__(self, other):
        pass

    def __cmp__(self, other):
        pass

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


ra = Ratio(1, 3)
print(ra + ra)
