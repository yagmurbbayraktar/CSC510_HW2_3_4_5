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
import unittest

class TestingSym(unittest.TestCase):
    def test_the(self):
         oo(the)

if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
