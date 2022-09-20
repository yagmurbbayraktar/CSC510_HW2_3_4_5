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

class TestingLIST(unittest.TestCase):
    def test_list(self):
        t = {}
        test_names = {'test_ls':1, 'test_bad':1, 'test_all':1, 'test_bigum': 1, 'test_csv': 1, 'test_data': 1, 
        'test_num': 1, 'test_stats': 1, 'test_sym': 1, 'test_the': 1
        }
        for i, (k, _) in enumerate(test_names.items()):
            t[i] = k
        t = [(i, v) for i, v in enumerate(sorted(t.values()))]
        t = dict(t)
        return t

if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

