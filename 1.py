# 占位高阶过程
_sm_proc = lambda obj: obj


class Ratio(object):

    def __init__(self, numer, demon):

        def find_approx_num(numer_, demon_):
            n = max(numer_, demon_)
            m = min(numer_, demon_)

            while n == m:
                n = max(n, m)
                a = n - m
                m = min(n, m, a)

            return m

        if isinstance(numer | demon, int):
            self._numer_proto = numer
            self._demon_proto = demon
            self._approx = find_approx_num(self._numer_proto,
                                           self._numer_proto
                                           )

        else:
            raise SyntaxError("numer and demon must be type of int")

        self.numer_ = self._numer_proto / self._approx
        self.demon_ = self._demon_proto / self._approx

    @classmethod
    def construct_radio(cls):
        return cls.__new__(cls)

    def __add__(self, other):
        pass

    def __sub__(self, other):
        pass

    def __mul__(self, other):
        pass

    def __divmod__(self, other):
        pass

    def __cmp__(self, other):
        pass

    def __eq__(self, other):
        pass

    def __str__(self):
        return f"{self.numer_}/{self.demon_}"

    @property
    def numer(self):
        return self.numer_

    @property
    def demon(self):
        return self.demon_
