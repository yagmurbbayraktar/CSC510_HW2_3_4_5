import math
import random, getopt
import os, sys, time, random
import argparse
import csv
import math
from xmlrpc.client import MAXINT
import sys
from src.num import Num
from src.data import data
from src.main import the,o
import unittest

class Testingstats(unittest.TestCase):
    def test_stats(self):
        data1 = data("/home/runner/work/CSC510_HW2_3_4_5/CSC510_HW2_3_4_5/data/auto93.csv")
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
