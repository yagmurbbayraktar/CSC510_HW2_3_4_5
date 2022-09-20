import sys
import sys
sys.path.insert(0, '/home/runner/work/CSC510_HW2_3_4_5/CSC510_HW2_3_4_5/src')
from num import Num
from main import the

def test_bignum():
        num = Num()
        the["nums"] = 32
        for i in range(1000):
            num.add(i)
        print(num.num().values())
        return 0 if(32 == len(num.has)) else 1

