import pytest
from num import Num
from coerce import the

def o(d):
    return str(d).replace(":", "").replace(",", ":").replace("'", "")

def oo(d):
	print(o(d))
	pass



class TestNum:

    def test_the(self):
        oo(the)
        assert True

    def test_num(self):
        numDict = {"Zom":[0,1,2,3,4,5,6,7,8,9]}
        for col, data in numDict.items():
            if col[0]:
                num = Num(0,col)
                for val in data:
                    num.add(val)


                number = num.nums()
                median = num.mid()
                sd = num.div()
                assert number == [0,1,2,3,4,5,6,7,8,9] and median == 5 and 3.1 <= sd and sd <= 4.1



