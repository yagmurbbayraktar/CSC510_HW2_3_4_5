import csv
import math
from xmlrpc.client import MAXINT

with open('Data.csv', 'r') as file:
    reader = csv.reader(file)
    data = []
    for row in reader:
        data.append(row)
print(data)

class num():
    def __init__(self, val, pos):
        self.count = 0 # counter
        self.has = {}  #stored data
        self.val = val  # value at key position
        self.pos = pos   # column position
        self.isSorted = True #boolean
        self.lo = MAXINT
        self.hi = -MAXINT

    def add(self, x, pos):
        if x != "?":
            self.count += 1
            self.lo = min(x, self.lo)
            self.hi = max(x, self.hi)

            # RESERVIOR SAMPLER AND ADD CODE TO BE WRITTEN

    def num(self):
        if not self.isSorted:
            self.has = {j: i for j, i in sorted(self.has.items(), key=lambda item: item[1])}
            self.isSorted = True
        return self.has

    def div(self):
        size = len(self.num())
        ninetieth_percentile = self.num()[int(math.ceil((size * 90) / 100)) - 1]
        tenth_percentile = self.num()[int(math.ceil((size * 10) / 100)) - 1]
        return (ninetieth_percentile - tenth_percentile) / 2.58

    def mid(self):
        temp = self.has
        return temp[(temp.len()-1)/2]




