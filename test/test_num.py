import math
import random, getopt
import os, sys, time, random
import argparse
import csv
import math
from xmlrpc.client import MAXINT
from CSC510_HW2_3_4_5.src.main import the
from CSC510_HW2_3_4_5.src.Num import Num
import unittest

class TestingNum(unittest.TestCase):
    def test_bignum(self):
        num = Num()
        the["nums"] = 32
        for i in range(1000):
            num.add(i)
        assert 32 == len(num.has)


if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
