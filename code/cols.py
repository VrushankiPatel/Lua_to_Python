from sym import Sym
from num import Num

class Cols:
    def __init__(self, names):
        self.names = names
        self.all = []      #columns
        self.klass = None  #
        self.x = []
        self.y = []
        
        #iterate name and index
        for c, s in enumerate(names):
            col = Num(c, s) if s[0].isupper() else Sym(c,s)
            self.all.append(col)
            
            if s[-1] != ":":
                if s[-1] in ['+', '-', '!']:
                    self.y.append(col)
                else:
                    self.x.append(col)
                
                if s[-1] == ":":
                    self.klass = col

def push(t, x):
    t[1+len(t)] = x
    return x