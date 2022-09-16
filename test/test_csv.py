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
from src.row import Row
from src.data import csv
import unittest

class TestingCSV(unittest.TestCase):
    def test_csv(self):
        n = 0
        while n < 10:
            csv("/home/runner/work/CSC510_HW2_3_4_5/CSC510_HW2_3_4_5/data/auto93.csv", Row)
            n += 1
            assert oo(Row) == print(Row)
        assert True

if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
