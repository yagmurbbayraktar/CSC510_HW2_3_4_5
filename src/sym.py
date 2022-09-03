import math
class Sym: #A stream of symbols

    def __init__(self, c = 0, s = ""):
        self.at = c #column position
        self.n = 0 #items seen
        self.name = s #column name
        self._has = {} #kept data
    #Add one thing to `col`. For Num, keep at most `nums` items.    
    def add(self, v = ""):
        if v != "?":
            self.n = self.n + 1
            if v in self._has.keys():
                self._has[v] += 1
            else:
                self._has[v] = 1

    def mid(self):
        most = -1
        most_key = ""
        for k, v in self._has.items():
            if v > most:
                most = v
                most_key = k
        return most, most_keys
        
        
    def div(self):
        e = 0
        for k, v in self._has.items():
            if v > 0:
                p = v/self.n
                e_f = p*math.log(p,2)
                e = e - e_f         
        return e
 

#short main to test the file 

#symbol = Sym()
#sym_list = ["a","a","a","a","b","b","c"]
#for s in sym_list:
#    symbol.add(s)
#mode = symbol.mid()
#entropy = symbol.div()
#print(mode)
#print(entropy)