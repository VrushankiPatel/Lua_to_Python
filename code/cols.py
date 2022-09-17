from num import Num
from sym import Sym

class cols:
    def __init__(self, names):
        self.names = names
        self.columns = []
        self.klass = None
        self.x_columns = []
        self.y_columns = []
        # iterate through names and also index
        for i, name in enumerate(names):
            # if the name starts with an uppercase letter, it is Numeric
            col = Num(i, name) if name[0].isupper() else Sym(i, name)
            self.columns.append(col)
            
            # if it doesn't end with a :,
            if name[-1] != ':':
                # add it as a dependent (Y) column if it ends with +, -, or !, or independent (X) otherwise
                if name[-1] in ['+', '-', '!']:
                    self.y_columns.append(col)
                else:
                    self.x_columns.append(col)
                
                # if the name ends with !, it is the klass column
                if name[-1] == '!':
                    self.klass = col