import math
import random, getopt
import os, sys, time, random
import argparse
import csv
import math
from xmlrpc.client import MAXINT
import sys
sys.path.append( '.' )
from src.main import the, oo
from src.num import Num
import unittest

class TestingCSV(unittest.TestCase):
    def test_csv(self):
        n = 0
        assert csv("../data/auto93.csv", row())
        for i in range(100):
            num.add(i)
        mid, div = num.mid(), num.div()
        print("div", div)
        print("mid", mid)
        assert 50 <= mid and mid <= 52 and 30.5 < div and div< 32

if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
