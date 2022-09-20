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
def cli(dump,inputfile, nums,seed,seperator):   #General sample of cli function talked about in class
        the = {}                                #The function takes several parameters and does updates on 'the' class/dictionary
        the["dump"]=dump                        #returns 'the' dictionary
        the["inputfile"]=inputfile
        the["nums"]=nums
        the["seed"]=seed
        the["seperator"]=seperator
        return the
    
def copy(t):   #Copy function 
        if not isinstance(t, dict):          
            return t
        u = {}
        for k in len(t):
            u[k] = t[k]
        return u

"""class the():
    def __init__(self, dump,inputfile, nums,seed,seperator):
        self.inputfile = inputfile
        self.nums = nums
        self.seed = seed
        self.seperator = seperator
        self.dump = dump"""
        
        
def o(t):
    pass

def oo(t):
    print(t)


def runs(k,old,status,out,msg):                 #'run' function is used to run all the eg.test cases and will be completeted in the following weeks
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

def coerce(str):
    if not isinstance(str, float):
        try:
            float(str)
            return float(str)
        except:
            return str
    elif str == "true":
        return True
    elif str == "false":
        return False
    else:
        return str
   
def csv(inputfile, result):
    sep = the["seperator"]
    with open(inputfile, "r") as f:
        for line in f.readlines():
            list = []
            for value in line.split(sep):
                list.append(coerce(value.strip()))
            result(list)

def push(input, row):
    input[1+len(input)]= row
    return row
            
       
if __name__ == '__main__':
        print ('Program start\n-----------------------------------------------')#signal of program starting
        try:                                                                    
            opts, args = getopt.getopt(sys.argv[1:],"hedf:n:s:S:", ["help", "eg","dump","file","nums","seed", "seperator"])
                                                                                #getopt module helps organize all parameters in cmd
                                                                                #that if input: $python -f            without any filename attached
                                                                                #cmd will print out the error message
        except getopt.GetoptError:
            print ('Wrong parameter usage')
            print ('test.py -f <inputfile> -n <nums> ........')
            print ('Input -h for help manual')
            sys.exit(2)
        for opt, arg in opts:
            if opt in ("-e", "--eg"):
                print ('start-up example, doing nothing')
                print('----------------------------------------------')
                sys.exit()
            elif opt in ("-h", "--help"):                                       #help manual given by the source code
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
        the = cli(dump,inputfile,nums,seed,seperator)
