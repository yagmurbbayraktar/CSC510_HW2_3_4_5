import math
import random, getopt
import os, sys, time, random
import argparse
import csv
import math
from xmlrpc.client import MAXINT
import sys
sys.path.insert(0, '/home/runner/work/CSC510_HW2_3_4_5/CSC510_HW2_3_4_5')
from src.num import Num
from src.data import data
from src.main import the,o
import unittest

def test_stats():
        data1 = data("/home/runner/work/CSC510_HW2_3_4_5/CSC510_HW2_3_4_5/data/auto93.csv")
        print('xmid= ', data1.stats(2, data1.cols.x, "mid"))
        print('xdiv= ', data1.stats(3, data1.cols.x, "div"))
        print('ymid= ', data1.stats(2, data1.cols.y, "mid"))
        print('ymid= ', data1.stats(3, data1.cols.y, "div"))
        return 0

