import sys
sys.path.insert(0, '../src')
from num import Num
from main import the

def test_num():
        num = Num()
        for i in range(100):
            num.add(i)
        print(num.num().values())
        mid, div = num.mid(), num.div()
        print("div", div)
        print("mid", mid)
        return 0 if (50 <= mid and mid <= 52 and 30.5 < div and div< 32) else 1
