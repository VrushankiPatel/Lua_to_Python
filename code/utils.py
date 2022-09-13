import math
import re
from typing import Callable


def coerce(self, s):
        def fun(s1):
            if s1.lower()=='true':
                return True
            if s1.lower()=='false':
                return False
            return s1
        if s.isdigit(): 
            return int(s)
        try: 
            float(s)
            return float(s)
        except ValueError: 
            return fun(re.match("^\s*(.*?)\s*$", s).groups()[0])

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


def push(t: dict, x):
    t[len(t) + 1] = x

    return x


def csv(fname: str, fun: Callable):
    sep = ","
    stream = open(fname, mode='r')

    while True:
        s = stream.readline()

        if not s:
            break
        else:
            t = [coerce(s1) for s1 in s.split(sep)]
            fun(t)
