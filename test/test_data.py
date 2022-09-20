import sys
sys.path.insert(0, '/home/runner/work/CSC510_HW2_3_4_5/CSC510_HW2_3_4_5/src')
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
        oo(col)
    return 0 if len(data1.cols.y) == 3 else 1
