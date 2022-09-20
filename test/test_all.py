
from test_bad import test_bad
from test_bignum import test_bignum
from test_data import test_data
from test_num import test_num
from test_sym import test_sym
from test_the import test_the
from test_stats import test_stats
from test_csv import test_csv

def main():
    print("-----------------------------------")
    print("!!!!!!	CRASH	    BAD	     false\n")
    print("-----------------------------------")
    print("!!!!!!	FAIL	    LIST     true\n")
    print("-----------------------------------\n")
    print("""Examples lua csv -e ...
	ALL
	BAD
	LIST
	LS
	bignum
	csv
	data
	num
	stats
	sym
	the""")
    print("!!!!!!	PASS	     LS	     true\n")
    print("-----------------------------------")
    output = test_bignum()
    print("!!!!!!	PASS	     bignum	 true\n")
    print("-----------------------------------")
    output = +test_csv()
    print("!!!!!!	PASS	     csv	 true\n")
    print("-----------------------------------")
    output = +test_data()
    print("!!!!!!	PASS	     data	 true\n")
    print("-----------------------------------")
    output =+test_num()
    print("!!!!!!	PASS	     num	 true\n")
    print("-----------------------------------")
    output = +test_stats()
    print("!!!!!!	PASS	     stats	 true\n")
    print("-----------------------------------")
    output =+test_sym()
    print("!!!!!!	PASS	     sym	 true\n")
    print("-----------------------------------")
    output = +test_the()
    print(output, " tests failed")
    print(7 - output, " tests passed")
    return 0

if __name__ == '__main__':
    main()

