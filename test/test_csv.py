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

def test_csv():
        n = 0
        data = csv("/home/runner/work/CSC510_HW2_3_4_5/CSC510_HW2_3_4_5/data/auto93.csv", Row)
        while n < 10:
            assert oo(Row(n) == print(Row(n)))
            n += 1
        return 0
