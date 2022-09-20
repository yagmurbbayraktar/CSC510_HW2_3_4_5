import sys
sys.path.insert(0, '/home/runner/work/CSC510_HW2_3_4_5/CSC510_HW2_3_4_5')
from src.main import the,oo
from src.data import data
import math
import random, getopt
import os, sys, time, random
import argparse
import csv
import math

def test_data():
    data1 = data("/home/runner/work/CSC510_HW2_3_4_5/CSC510_HW2_3_4_5/data/auto93.csv")
    for _, col in enumerate(data1.cols.y):
        print("{:at ", col.at, ":hi ", col.hi, ":lo ", col.lo, ":isSorted ", col.isSorted,":n ", col.count, ":name ", col.name, "}")
    print(len(data1.cols.y))
    return 0 
