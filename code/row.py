def copydic(t):
    if ~isinstance(t,dict):
        return t
    u = {}
    for k in t:
        u[k] = copydic(t[k])
    return u

    
    
class row:
    def __init__(self,t={}):
        self.cells = t
        self.cooked = copydic(t)
        self.isEvaled = False
