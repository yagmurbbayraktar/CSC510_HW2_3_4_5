import math
import random, getopt
import os, sys, time, random
import argparse
import csv
import math
from xmlrpc.client import MAXINT
from main import the

def per(t,p):
        p = math.floor(((p or 0.5)*len(t))+0.5)
        return t[max(1, min(len(t),p))]

class Num():
    def __init__(self, val = ""):
        self.count = 0 # counter
        self.has = {}  #stored data
        self.val = val  # value at key position
        self.isSorted = False #boolean
        self.lo = MAXINT
        self.hi = -MAXINT

    def add(self,v):
        if v!="?":
            self.count = self.count+1
            self.lo = min(v, self.lo)
            self.hi = max(v, self.hi)
            length = len(self.has)
            pos = -1
            if length < the["nums"]:
                pos = 1+length
            elif random.random() < the["nums"]/ self.count:
                pos = random.randint(1,length)
            if pos >= 0:
                self.isSorted = False 
                self.has[pos]=float(v)

    def num(self):
        if self.isSorted == False:
            self.has = {j: i for j, i in sorted(self.has.items(), key=lambda item: item[1])}
            self.isSorted = True
        return self.has

    def div(self):
        diction = self.num()
        size = len(diction)
        
        ninetieth_percentile = per(list(diction.values()), 0.9)
        tenth_percentile = per(list(diction.values()), 0.1)
        
        return (ninetieth_percentile - tenth_percentile) / 2.58

    def mid(self):
        lst = self.num()
        return per(list(self.num().values()), 0.5)
