from data import Data
from utils import csv, oo, o


# def test_csv():
#     class TenRowTester:
#         n = 0

#         def print(self, row):
#             self.n += 1

#             if self.n > 10:
#                 return
#             else:
#                 oo(row)

#     row_tester = TenRowTester()
#     csv("csv.csv", row_tester.print)

#     return True


# def test_data():
#     d = Data("data/csv.csv")
#
#     for _, col in d.cols.y.items():
#         oo(col)
#
#     return True
#
#
# def test_stats():
#     data = Data("data/csv.csv")
#
#     def div(col):
#         return col.div()
#
#     def mid(col):
#         return col.mid()
#
#     print("xmid", o(data.stats(2, data.cols.x, mid)))
#     print("xdiv", o(data.stats(3, data.cols.x, div)))
#     print("ymid", o(data.stats(2, data.cols.y, mid)))
#     print("ydiv", o(data.stats(3, data.cols.y, div)))
#
#     return True


if __name__ == '__main__':
    pass
    #test_csv()
