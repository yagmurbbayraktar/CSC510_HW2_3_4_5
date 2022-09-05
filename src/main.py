import math
import random, getopt
import os, sys, time, random
import argparse
import csv
import math
from xmlrpc.client import MAXINT
import unittest

eg, fails = {}, 0
inputfile = 'data.csv'
nums = 512
seed = 10019
seperator = ",]]"
dump = False
the = {}
the["dump"]=dump
the["inputfile"]=inputfile
the["nums"]=nums
the["seed"]=seed
the["seperator"]=seperator


"""
def o(t,show,u):
    if type(t) != "table":
        return str(t)
    elif
def oo(t):
    print(o(t))
    return t
"""
def theform(dump,inputfile, nums,seed,seperator):
        the = {}
        the["dump"]=dump
        the["inputfile"]=inputfile
        the["nums"]=nums
        the["seed"]=seed
        the["seperator"]=seperator
        return the

"""class the():
    def __init__(self, dump,inputfile, nums,seed,seperator):
        self.inputfile = inputfile
        self.nums = nums
        self.seed = seed
        self.seperator = seperator
        self.dump = dump"""
        
        
"""def o(t):
    if not isinstance(t, dict):
        return str(t)
    def show(k, v):
        if str(k).find("^_") == -1:
        v = o(v)
        return ":{0} {1}".format(k, v) if len(t) != 0 else str(v)
    
    u = []
    for k, v in t.items():
        u.append(show(k, v))
    if len(t) == 0:
        sorted(u)
    return "{" + " ".join(u) + "}"

def oo(t):
    disp = o(t)
    print(disp)
"""

def runs(k,old,status,out,msg):
    if not eg[k]:
        return
    random.seed(the.seed)
    old =[]
    num = 0
    for i in the:
        old[num] = i
        num = num + 1
    if the.dump:
        status,out = True, eg[k]
    else:
        try:
            status,out = True, eg[k]
        except:
            out = "Exception thrown. eg does not exist."
    num1 = 0
    for j in old:
        the[num1] = j
        num1 = num1 + 1
    msg = status and ((out == True and "PASS") or "FAIL") or "CRASH"
    print("!!!!!!", msg, k , status)
    return out

def csv1(inputfile):
    dict = {}
    with open(inputfile, 'r') as file:
        content = [line[:-1] for line in file]
    header = (content[:1][0]).split(',')
    rows = content[1:]

    for index in range(len(header)):
        rowArray = []
        for row in rows:
            rowArray.append(row[index])
        dict[header[index]] = rowArray

    print(header)

if __name__ == '__main__':
        print ('Program start\n-----------------------------------------------')
        try:
            opts, args = getopt.getopt(sys.argv[1:],"hedf:n:s:S:", ["help", "eg","dump","file","nums","seed", "seperator"])
        except getopt.GetoptError:
            print ('test.py -f <inputfile> -n <nums> ........')
            sys.exit(2)
        for opt, arg in opts:
            if opt in ("-e", "--eg"):
                print ('start-up example, doing nothing')
                print('----------------------------------------------')
                sys.exit()
            elif opt in ("-h", "--help"):
                print ("""OPTIONS:
                    -e      --eg            startup example                     = nothing
                    -d      --dump          on test fail, exit with startdump   = false
                    -f      --file          file with csv data                  = data.csv
                    -h      --help          show help                           = false
                    -n      --nums          number of nums to keep              = 512
                    -s      --seed          random number seed                  = 10019
                    -S      --seperator     field seperator                     = ,]]""")
                print('----------------------------------------------')
                sys.exit()
            elif opt in ("-d", "--dump"):
                print ('True (incompleted)')
                dump = True
                print('----------------------------------------------')
                sys.exit()
            elif opt in ("-f", "--file"):
                inputfile = arg
            elif opt in ("-n", "--nums"):
                nums = arg
            elif opt in ("-s", "--seed"):
                seed = arg
            elif opt in ("-S", "--seperator"):
                seperator = arg
        the = theform(dump,inputfile,nums,seed,seperator)
        csv1(inputfile)