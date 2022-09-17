from sym import Sym
from num import Num

class cols:
    def __init__(self, names):
        self.names = names
        self.all = {}      #columns
        self.klass = {}  #
        self.x = {}
        self.y = {}
        
        for index, name in enumerate(names):
            
            if name.istitle():
                curCol = push(self.all, Num(index, name))
                print(curCol)
            else:
                curCol = push(self.all, Sym(index, name))    
            
            if name[-1] != ":":
                if "+" in name or "-" in name:
                    push(self.y, curCol)
                else:
                    push(self.x, curCol)
                
                if name[-1] == "!":
                    self.klass = name

def push(t, x):
    t[1+len(t)] = x
    return x