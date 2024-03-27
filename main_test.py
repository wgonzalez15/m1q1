import main
import io
import sys
import re
import math


def test_main_1():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    # datastr = '10 5 20 0 40 45 50 55 9 10\n'
    datastr = '1 2 3 4 5 6'
    sys.stdin = io.StringIO(datastr)

    result = main.main()
    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    print(f'Your return value is {result}')
    assert result[0] == 7
    assert result[1] == 7
    assert result[2] == 7


def test_main_2():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    # datastr = '10 5 20 0 40 45 50 55 9 10\n'
    # datastr = '2\n4\n6\n5\n8\n10\n11\n12\n14\n20'
    datastr = '1 2 3 4 5 5 4 3 2 1'
    sys.stdin = io.StringIO(datastr)

    result = main.main()
    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)
    print(f'Your return value is {result}')
    assert result[0] == 2
    assert result[1] == 4
    assert result[2] == 6
    assert result[3] == 8
    assert result[4] == 10
