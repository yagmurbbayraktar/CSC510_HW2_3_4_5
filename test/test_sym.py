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
from src.sym import Sym
import unittest

class TestingSym(unittest.TestCase):
    def test_sym(self):
        sym = Sym()
        for item in ["a", "a", "a", "a", "b", "b", "c"]:
            sym.add(item)
        mode, entropy = sym.mid(), sym.div()
        entropy = (1000*entropy)//(1/1000)
        print('mid:', mode, 'div:', entropy)
        assert mode=="a" and 1.37<=entropy and entropy<=1.38

if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
