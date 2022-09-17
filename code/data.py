from cols import Cols
from utils import push, csv,the,o,oo,rnd
from num import Num
from row import row

class Data:        
    def __init__(self, src):
        self.cols = None
        self.rows = {}
        if type(src)==type('string'):
            csv(src,lambda row:self.add(row))
        else:
            for _,row in enumerate(src or {}):
                self.add(row)


    def stats(self,places,showCols, fun):
        showCols , fun = showCols or self.cols.y, fun or Num.mid()
        t = {};
        for col in showCols.values():
            v = fun(col)
            v = type(v) == type(0) and rnd(v,places) or v
            t[col.name] = v
        return t
    
    def add(self,xs):
        if self.cols == None:
            value_list = list(xs.values())
            self.cols = Cols(value_list)
        else:
            row1 = row(xs)
            row1 = push(self.rows,row1)
            # need to be fixed
            for _, todo in enumerate([self.cols.x,self.cols.y]):
                #print(todo)
                for col in todo.values():
                    #print(type(col))
                    col.add(row1.cells[col.at])


def test_csv():
    class TenRowTester:
        n = 0
        def print(self, row):
            self.n += 1
            if self.n > 10:
                return
            else:
                oo(row)
    row_tester = TenRowTester()
    csv("csv.csv", row_tester.print)

    return True
def test_data():
    d = Data(the().func_the()["file"])
    for c in d.cols.y.values(): oo(c)
    assert True


def test_stats():
    data = Data(the().func_the()["file"])
    print("xmid", o( data.stats(2, data.cols.x, lambda col:col.mid())))
    print("xdiv", o( data.stats(3, data.cols.x, lambda col:col.div())))
    print("ymid", o( data.stats(2, data.cols.y, lambda col:col.mid())))
    print("ydiv", o( data.stats(3, data.cols.y, lambda col:col.div())))
    assert True

test_csv()
test_data()
test_stats()