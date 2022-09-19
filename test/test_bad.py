from cgi import test


def test_bad():
    raise ValueError('Intentional bad test was run. The world just crashed.')

test_bad()