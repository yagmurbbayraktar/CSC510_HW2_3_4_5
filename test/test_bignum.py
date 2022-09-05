import math
import random, getopt
import os, sys, time, random
import argparse
import csv
import math
from xmlrpc.client import MAXINT
from CSC510_HW2_3_4_5.src.main import the
from CSC510_HW2_3_4_5.src.Num import Num
import unittest

class TestingBignum(unittest.TestCase):
    def test_num(self):
        num = Num()
        for i in range(100):
            num.add(i)
        mid, div = num.mid(), num.div()
        print("div", div)
        print("mid", mid)
        assert 50 <= mid and mid <= 52 and 30.5 < div and div< 32

if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
