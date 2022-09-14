
s = __file__
s = s[0:len(s)-19]
s = s+"/src"
import sys
sys.path.insert(1, s)
from num import Num
from main import the

def test_bignum():
        num = Num()
        the["nums"] = 32
        for i in range(1000):
            num.add(i)
        return 0 if(32 == len(num.has)) else 1

