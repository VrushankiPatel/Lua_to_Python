from typing import Callable
from row import row
from cols import Cols
from utils import coerce
from utils import push,csv

class Data:        
    def _init_(self, src):
        self.cols = None   # summaries of data
        self.rows = {}   # kept data

        def add_(row: str):
            self.add(row)

        if type(src) == str:
            csv(src, add_)
    
    def add(self, xs):
        if self.cols is None:
            self.cols = Cols(xs)
        else:
            row = push(self.rows, xs.cells and xs or self.add(xs))



if _name_ == "_main_":
    data=Data("csv.csv")
