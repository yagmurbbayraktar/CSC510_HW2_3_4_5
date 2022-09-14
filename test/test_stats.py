import math
import random, getopt
import os, sys, time, random
import argparse
import csv
import math
from xmlrpc.client import MAXINT
s = __file__
s = s[0:len(s)-17]
s = s+"/src"
import sys
sys.path.insert(1, s)
from num import Num
from data import data
from main import the,o
import unittest

class Testingstats(unittest.TestCase):
    def test_stats(self):
        data1 = data("../data/auto93.csv")
        def div(col):
            return col.div()
        def mid(col):
            return col.mid()
        print("xmid", o(data1.stats(2, data1.cols.x, mid)))
        print("xdiv", o(data1.stats(3, data1.cols.x, div)))
        print("ymid", o(data1.stats(2, data1.cols.y, mid)))
        print("ydiv", o(data1.stats(3, data1.cols.y, div)))
        assert True


if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
