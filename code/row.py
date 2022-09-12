import copy



# ‘Row‘ holds one record
class row:
    def __init__(self, t):
        self.cells = t,  # one record
        self.cooked = copy.deepcopy(t)  # used if we discretize data
        self.isEvaled = False  # true if y−values evaluated