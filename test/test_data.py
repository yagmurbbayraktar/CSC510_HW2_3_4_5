
s = __file__
s = s[0:len(s)-16]
s = s+"/src"
import sys
sys.path.insert(1, s)
from main import the,oo
from data import data
import math
import random, getopt
import os, sys, time, random
import argparse
import csv
import math

def test_data():
    data1 = data("../data/data1.csv")
    for _, col in enumerate(data1.cols.y):
        oo(col)
    return 0 if len(data1.cols.y) == 3 else 1
