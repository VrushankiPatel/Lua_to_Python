from sym import Sym
from num import Num

class Cols:
    def __init__(self, names):
        self.names = names
        self.all = {}      #columns
        self.klass = {}  #
        self.x = {}
        self.y = {}
        
        #iterate name and index
        for c, s in enumerate(names):
            if name.istitle():
                curCol = push(self.all, Num(c,s))
            else:
                curCol = push(self.all, Sym(c,s)) 
            
            if s[-1] != ":":
                if s[-1] in ['+', '-']:
                    push(self.y, curCol)
                else:
                    push(self.x, curCol)
                
                if s[-1] == ":":
                    self.klass = name

def push(t, x):
    t[1+len(t)] = x
    return x
