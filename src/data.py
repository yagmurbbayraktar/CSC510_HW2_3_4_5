from csv import reader
from cols import Cols
from main import the, push, csv
from row import Row
import re

class data:
    def __init__(self, src):
        self.cols = None #summaries of data
        self.rows = {} #kept data
        if isinstance(src, str):
            csv(src, self.add)
        else:
            for _, row in enumerate(src or {}):
                self.add(row)
                
    def add(self, xs):
        if not self.cols:
            self.cols = Cols(xs)
        else:
            row = push(self.rows, Row(xs))
            for _, todo in enumerate([self.cols.x, self.cols.y]):
                for _, col in enumerate(todo):
                    col.add(row.cells[col.at])
                    
    def stats(self, places, showcols, fun):
        places = places or 2
        showcols = showcols or self.cols.y 
        fun = fun or "mid"
        t = {}       
        for _, col in enumerate(showcols):
            v = 0
            if fun == "mid":
                v = col.mid()
            else:
                v = col.div()
            v = round(v, places)
            t[col.name] = v
        return t


someStringCHANGE = "" #will come from another part of code.
"""# Call `fun` on each row. Row cells are divided in `the.seperator`.
def csv(fname, fun):
    sep = "([^" + someStringCHANGE + "]+)"
    try:
        f = open(fname, 'r')
    except:
        import os
        f = open(str(os.path.dirname(__file__)) + "/../data/" +str(fname))
    csv_reader = reader(f)
    for row in csv_reader:
        t = []
        for s1 in re.findall(row, sep):
            t.append(s1) #coerce function will come here i dont have it yet. CHANGE
        fun(t)

def coerce(s):
    def fun(s1):
        if s1:
            return True
        else:
            return False
    a = 0
    if type(s) == int:
        return int(s)
    elif type(s) == float:
        return float(s)
    else:
        x = re.search(r"^\s*(.*)\s*$", s)
        return fun(x.group())



# function coerce(s,    fun)
#   function fun(s1)
#     if s1=="true"  then return true end 
#     if s1=="false" then return false end
#     return s1 end 
#   return math.tointeger(s) or tonumber(s) or fun(s:match"^%s*(.-)%s*$") end





# -- Call `fun` on each row. Row cells are divided in `the.seperator`.
# function csv(fname,fun,      sep,src,s,t)
#   sep = "([^" .. the.seperator .. "]+)"
#   src = io.input(fname)
#   while true do
#     s = io.read()
#     if not s then return io.close(src) else 
#       t={}
#       for s1 in s:gmatch(sep) do t[1+#t] = coerce(s1) end
#       fun(t) end end end
"""
