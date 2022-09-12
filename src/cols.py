import re
from src.num import Num
from src.sym import Sym

class Cols:
    def _init_(self, names):
        self.names = names
        self.all = []
        self.x =[]
        self.y = []
        self.klass = None
    
    def cols(self):
        for c in range(len(self.names)):
            if (re.search('^[A-Z]', self.names[c])):
                col = Num(c, self.names[c])
                self.all.append(Num(c, self.names[c]))
            else:
                col = Sym(c, self.names[c])
                self.all.append(Sym(c, self.names[c]))
            
            if not re.search(':$', self.names[c]):
                if re.search('[!+-]'):
                    self.y.append(Num(c, self.names[c]))
                else:
                    self.x.append(Sym(c, self.names[c]))
                
                if re.search('!$', self.names[c]):
                    self.klass = col

