
def copyd(t):
    if ~isinstance(t,dict):
        return t
    u = {}
    for k in t:
        u[k] = copyd(t[k])
    return u

# ‘Row‘ holds one record
class row:
    def __init__(self, t={}):
        self.cells = t,  # one record
        self.cooked = copyd(t)  # used if we discretize data
        self.isEvaled = False  # true if y−values evaluated
