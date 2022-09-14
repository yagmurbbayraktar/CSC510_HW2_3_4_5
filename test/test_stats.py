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
from data import Data
from main import the,o
import unittest

class Testingstats(unittest.TestCase):
    def test_stats(self):
        data = Data("../data/auto93.csv")
        def div(col):
            return col.div()
        def mid(col):
            return col.mid()
        print("xmid", o(data.stats(2, data.cols.x, mid)))
        print("xdiv", o(data.stats(3, data.cols.x, div)))
        print("ymid", o(data.stats(2, data.cols.y, mid)))
        print("ydiv", o(data.stats(3, data.cols.y, div)))
        assert True


if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
