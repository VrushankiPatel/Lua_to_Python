
import pytest
from sym import Sym

class TestReturn:

    def test_sym(self):
        symDict = {"Waol":["@","@","$","*"]}
        for col , data in symDict.items():
            if col[0]:
                sym = Sym(0,col)
                for val in data:
                    sym.add(val)
                entropy = sym.div()
                mode = sym.mid()
                assert entropy == 1.5 and mode == "@"

