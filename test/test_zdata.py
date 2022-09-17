from cols import cols
from utils import push, csv,the,o,oo,rnd
from num import Num
from row import row
from data import Data

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


def test_csv():
    class TenRowTester:
        n = 0
        def print(self, row):
            self.n += 1
            if self.n > 10:
                return
            else:
                oo(row)
    row_tester = TenRowTester()
    csv("csv.csv", row_tester.print)

    return True
def test_data():
    d = Data(the().func_the()["file"])
    for c in d.cols.y.values(): oo(c)
    assert True


def test_stats():
    data = Data(the().func_the()["file"])
    print("xmid", o( data.stats(2, data.cols.x, lambda col:col.mid())))
    print("xdiv", o( data.stats(3, data.cols.x, lambda col:col.div())))
    print("ymid", o( data.stats(2, data.cols.y, lambda col:col.mid())))
    print("ydiv", o( data.stats(3, data.cols.y, lambda col:col.div())))
    assert True

#test_csv()
#test_data()
#test_stats()