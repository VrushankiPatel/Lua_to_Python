import random
import math


class Num:
    '''
        'Num's summarize a stream of symbols.

        Usage:
        num = Num()
    '''

    n = 0
    at = 0
    name = ""
    _has = []  # as per Sym
    

    lo = math.inf  # lowest seen
    hi = -math.inf  # highest seen
    isSorted = True  # no updates since last sort data


    def __init__(self, c=0, s=""):
        '''
                Creates Num object.

                :param c: Position of the column
                :param s: Name of the column
        '''

        if c:
            self.at = c

        if s:
            self.name = s

        if (s == ""):
            w = 0
        elif (s[-1] == '+'):
            w = 1
        elif (s[-1] == '-'):
            w = -1
        else:
            w = 0

    def nums(self):
        '''
        Returns Kept numbers, sorted.
        :return:
        '''

        if self.isSorted == False:
            self._has.sort()
            self.isSorted = True

        return self._has


    # Reservoir sampler
    def add(self, v):
        '''
                Add number to distribution.

                :param v: number to add
        '''
        the = {'nums':50}
        if v != '?':
            self.n = self.n + 1
            self.lo = min(self.lo, v)
            self.hi = max(self.hi, v)
            if len(self._has) < the['nums']:
                pos = 1 + len(self._has)
                self._has.append(v)
            elif random.random() < the['nums'] / self.n:
                pos = random.randint(0, the['nums'] - 1)
                self._has[pos] = v
            else:
                pos = -1
            if pos != -1:
                self.isSorted = False

    def div(self):
        '''
        Diversity: Standard Deviation for Nums
        :return:
        '''

        a = self.nums()
        in9 = int(len(a) * 0.9)  # index 90
        in10 = int(len(a) * 0.1)  # index 10

        return (a[in9] - a[in10]) / 2.58

    def mid(self):
        '''
        Central tendancy: median for Nums
        :return:
        '''

        a = self.nums()
        in50 = int(len(a) * 0.5)  # index 50
        
        return a[in50]
    
if __name__ == '__main__':
    x = Num(c = 5, s = "Zom")
    for i in range(10):
        x.add(i)

    print(x.nums())
    print(x.mid())
    print(x.div())
