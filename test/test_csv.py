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
n = 0
def test_csv():
        def row(input):
                n+=1
                global n
                if n >10:
                        return
                else:
                        print(input)
        data = csv("/home/runner/work/CSC510_HW2_3_4_5/CSC510_HW2_3_4_5/data/auto93.csv", row)
        return 0
