import math
import random, getopt
import os, sys, time, random
import argparse
import csv
import math
from xmlrpc.client import MAXINT
import sys
sys.path.append( '.' )
from src.main import the, oo, csv
from src.row import Row
import unittest

class TestingCSV(unittest.TestCase):
    def test_csv(self):
        n = 0
        data = csv("/home/runner/work/CSC510_HW2_3_4_5/CSC510_HW2_3_4_5/data/auto93.csv", Row)
        while n < 10:
            assert oo(Row(n) == print(Row(n)))
            n += 1
        assert True

if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
