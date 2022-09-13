from typing import Callable
from row import row
from cols import Cols
from utils import coerce
from utils import push,csv

'''
class Data:        
    def __init__(self, src):
        self.cols = None   # summaries of data
        self.rows = []   # kept data
        self.error = False

        def add_(row: str):
            self.add(row)

        if type(src) == str:
            csv(src, add_)
    
    def add(self, xs):
        if self.cols is None:
            self.cols = Cols(xs)
        else:
            row = push(self.rows, xs.cells and xs or self.add(xs))
'''

class Data:
    def __init__(self, src):
        self.cols = None   # summaries of data
        self.rows = []   # kept data
        self.error = False
        if (isinstance(src, str)):
            try:
                csv_file = open(src)
                csv_text = csv_file.read()
                self.rows = csv_text.split("\n")
                cols_names= self.rows[0].split(",")
                #print(cols_names)
                self.cols = Cols(cols_names)
                csv_file.close()
            except FileNotFoundError:
                self.error = True
                print("File", src, "does not exist")

if __name__ == "__main__":
    data=Data("csv.csv")