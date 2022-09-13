try:
    import sym
except ImportError as e:
    import sys
    sys.path.append("../src")

from main import oo

def test_the(argv):
    oo(argv)


if __name__=='__main__':
    test_the(argv='this-is-first-argument')
    
import math
import random, getopt
import os, sys, time, random
import argparse
import csv
import math
from xmlrpc.client import MAXINT
import sys
sys.path.append( '.' )
from src.main import the
import unittest

class TestingSym(unittest.TestCase):
    def test_the(self):
        sym = the()
        
        assert mode=="a" and 1.37<=entropy and entropy<=1.38

if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
