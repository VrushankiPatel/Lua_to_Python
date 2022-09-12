from sym import Sym
from num import Num


    
class Cols:
    def _init_(self, names):
        self.names = names
        self.all = {}
        self.klass = None  #{}
        self.x = {}
        self.y = {}
        
        for c, s in enumerate(names):
            if s.istitle():
                col = push(self.all, Num(c, s))
            else:
                col = push(self.all, Sym(c, s))    
            
            if s[-1] != ":":
                if "+" in s:
                    push(self.y, col)
                elif "-" in s:
                    push(self.x, col)
                
                if s[-1] == ":":
                    self.klass = col

def push(t, x):
    t[1+len(t)] = x
    return x