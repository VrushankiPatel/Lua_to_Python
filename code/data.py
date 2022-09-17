from cols import Cols
from utils import push, csv


class Data:        
    def __init__(self, src):
        self.cols = None   # summaries of data
        self.rows = []   # kept data
        self.error = False

        if type(src) == str:
            csv(src, self.add)
    
    def add(self, xs):
        if self.cols is None:
            self.cols = Cols(xs)
        else:
            row = push(self.rows, xs if len(xs) == 0 else self.add(xs))

            for _, todo in self.cols.x, self.cols.y:
                for _, col in todo.items():
                    col.add(row[col.at])

# class Data:
#     def __init__(self, src):
#         self.cols = None   # summaries of data
#         self.rows = []   # kept data
#         self.error = False
#         if (isinstance(src, str)):
#             try:
#                 csv(src, self.add)
#
#                 csv_file = open(src)
#                 csv_text = csv_file.read()
#                 self.rows = csv_text.split("\n")
#                 cols_names= self.rows[0].split(",")
#                 #print(cols_names)
#                 self.cols = Cols(cols_names)
#                 csv_file.close()
#             except FileNotFoundError:
#                 self.error = True
#                 print("File", src, "does not exist")