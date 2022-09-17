from cols import cols
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
            self.cols = cols(value_list)
        else:
            row1 = row(xs)
            row1 = push(self.rows,row1)
            # need to be fixed
            for _, todo in enumerate([self.cols.x,self.cols.y]):
                #print(todo)
                for col in todo.values():
                    #print(type(col))
                    col.add(row1.cells[col.at])
