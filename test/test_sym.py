import math
import random, getopt
import os, sys, time, random
import argparse
import csv
import math
from xmlrpc.client import MAXINT
import sys
sys.path.insert(0, '/home/runner/work/CSC510_HW2_3_4_5/CSC510_HW2_3_4_5')
from src.main import the
from src.sym import Sym
import unittest

def test_sym():
        sym = Sym()
        for item in ["a", "a", "a", "a", "b", "b", "c"]:
            sym.add(item)
        mode, entropy = sym.mid(), sym.div()
        entropy = (1000*entropy)//1/1000
        print('mid:', mode, 'div:', entropy)
        return 0 if( mode=="a" and 1.37<=entropy and entropy<=1.38) else 1
