try:
    import sym
except ImportError as e:
    import sys
    sys.path.append("../src")

import oo

def test_the(argv):
    return oo(argv)


if __name__=='__main__':
    print(test_the(argv=['this-is-first-argument']))
