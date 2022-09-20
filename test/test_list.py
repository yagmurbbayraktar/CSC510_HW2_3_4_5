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
    def test_list(self):
        t = {}
        test_names = {
        'ALL':1,
        'BAD':1,
        'LIST':1,
        'LS':1,
        'bignum':1,
        'csv':1,
        'data':1,
        'num':1,
        'stats':1,
        'sym':1,
        'the':1
        }
        for i, (k, _) in enumerate(test_names.items()):
            t[i] = k
        t = [(i, v) for i, v in enumerate(sorted(t.values()))]
        t = dict(t)
        return t

if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
