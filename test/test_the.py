try:
    import sym
except ImportError as e:
    import sys
    sys.path.append("../src")

from main import oo

def test_the(argv):
    oo(argv)


if __name__=='__main__':
    test_the(argv='this-is-first-argument')
