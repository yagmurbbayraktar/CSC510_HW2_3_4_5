try:
    import sym
except ImportError as e:
    import sys
    sys.path.append("../src")

import sym

def test_sym(sym_obj):
    for item in ["a", "a", "a", "a", "b", "b", "c"]:
        sym_obj.add(item)
    mode, entropy = sym_obj.mid(), sym_obj.div()
    entropy = (1000*entropy)//(1/1000)
    print('mid:', mode, 'div:', entropy)
    return mode=="a" and 1.37<=entropy and entropy<=1.38


if __name__=='__main__':
    sym_obj = sym.Sym()
    print(test_sym(sym_obj))
