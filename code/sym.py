import math


class Sym:
    """
    'Sym's summarize a stream of symbols.

    Usage:
        sym = Sym()

        sym.add("$") # Adds symbol '$' to the distribution
        sym.add("%") # Adds symbol '%' to the distribution
        sym.add("%") # Adds symbol '%' to the distribution

        print("Mode:", sym.mid()) # Print mode of the distribution
        print("Entropy:", sym.div()) # Print entropy of the distribution

    """
    n = 0

    at = 0
    name = ""

    _has = {}

    def __init__(self, c: int, s: str):
        """
        Creates Sym object.

        :param c: Position of the column
        :param s: Name of the column
        """

        if c:
            self.at = c

        if s:
            self.name = s

    def add(self, v: str):
        """
        Add symbol to distribution.

        :param v: symbol to add
        """
        if v != "?":
            self.n += 1
            self._has[v] = self._has.get(v, 0) + 1

    def mid(self) -> int:
        """
        Calculates mode of the distribution.

        :return: Mode of symbols present
        """
        mode = None
        most = -1

        for k, v in self._has.items():
            if v > most:
                mode, most = k, v

        return mode

    def div(self) -> int:
        """
        Calculates entropy of the distribution.

        :return: Entropy of the distribution
        """

        def fun(p):
            return p * math.log(p, 2)

        e = 0

        for _, n in self._has.items():
            if n > 0:
                e = e - fun(n / self.n)

        return e
