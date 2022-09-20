from test_bad import test_bad
from test_bignum import test_bignum
from test_csv import test_csv
from test_data import test_data
from test_LS import test_LS
from test_num import test_num
from test_sym import test_sym
from test_the import test_the
from test_stats import test_stats
from test_csv import test_csv

def main():test_stats()+
    output = test_bad()+test_bignum()+test_csv()+test_data()+test_LS()+test_num()+test_sym()+test_the()+test_stats()+test_csv()
    print(output, " tests failed")
    print(7 - output, " tests passed")
    return output

if __name__ == '__main__':
    main()

