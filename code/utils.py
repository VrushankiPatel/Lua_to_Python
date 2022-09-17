import math
import re
from typing import Callable, Any
from csv import reader


def rnd(x,places):
    mult = pow(10,(places or 2))
    return math.floor(x * mult +0.5)/mult


def coerce(s):
    def fun(s1):
        if s1.lower() == 'true':
            return True
        if s1.lower() == 'false':
            return False
        return s1

    if s.isdigit():
        return int(s)

    try:
        return float(s)

    except ValueError:
        return fun(re.match("^\\s*(.*?)\\s*$", s).groups()[0])


# def cli(t: dict):
#     for slot, v in t.items():
#         v = str(v)
#
#         for n, x in arg:
#             if x == "-" or x == "--":
#                 x.append(slot[1, 1])


def per(t: dict, p: int):
    p = math.floor((p or 0.5) * len(t) + 0.5)
    q = t[max(1, min(len(t), p))]

    return q


def push(t, x):
    t[1+len(t)] = x
    return x

def csv(fname, fun):
    sep = the().func_the()["seperator"]
    
    #src = open(fname)
    with open(fname,'r') as src:
        rdr = reader(src, delimiter=sep)
        for l in rdr:
            d={}
            for v in l:
                d[len(d)]=coerce(v)
            #print(d)
            fun(d)



#def o(t: Any):
    # if not isinstance(t, dict):
    #     return str(t)
    #
    # def show(_k, _v):
    #     if re.search(str(k), "^_") is not None:
    #         _v = o(_v)
    #
    #         return str.format(":%s %s", _k, _v) if len(t) == 0 else str(_v)
    #
    # u = {}
    #
    # for k, v in t.items():
    #     u[1 + len(u)] = show(k,v)
    #
    # if  len(t) == 0:
    #     table.sort(u)
    #
    # return "{" + table.concat(u, " ") +  "}"

    #return t

def o(d):
    return str(d).replace(":", "").replace(",", ":").replace("'", "")


def oo(d):
    print(o(d))
    pass



class the:
    def __init__(self) -> None:
        self.the = {}
        self.help = """CSV : summarized csv file
        (c) 2022 Tim Menzies <timm@ieee.org> BSD-2 license
        USAGE: lua seen.lua [OPTIONS]
        OPTIONS:
        -e  --eg        start-up example                      = nothing
        -d  --dump      on test failure, exit with stack dump = false
        -f  --file      file with csv data                    = csv.csv
        -h  --help      show help                             = false
        -n  --nums      number of nums to keep                = 512
        -s  --seed      random number seed                    = 10019
        -S  --seperator feild seperator                       = ,"""

    def func_the(self):
        help = self.help
        reexp = r"[-][\S]+[\s]+[-][-]([\S]+)[^\n]+= ([\S]+)"
        dictre = re.findall(reexp, help)
        for key, value in dictre:
            self.the[key] = coerce(value)
        return self.the


