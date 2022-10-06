import re
from num import Num
from main import push
from sym import Sym

class Cols:
    def __init__(self, names):
        self.names = names
        self.all = []
        self.x =[]
        self.y = []
        self.klass = None
    
        for c, s in enumerate(names): 
                    col = s[0].isupper() and Num(c, s) or Sym(c, s)  
                    push(self.all,col)
                    if s[-1] != ':':
                        push(self.y,col) if s[-1] == '-' or s[-1] == '+' else push(self.x,col)
                        if s[-1] == '!':
                            self.klass = col


