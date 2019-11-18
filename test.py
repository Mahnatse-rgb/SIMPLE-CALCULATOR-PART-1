#Using pytest to check the performance of my functions on the test_function.py file

from test_function import *

def test_addition():

    assert addition(0,0) == 0
    assert addition(-1,-1) == -2
    assert addition(4,5) == 9
    assert addition(1,2,3,4) == 10

def test_multiplying():

    assert multiplying(1,2) == 2
    assert multiplying(-1,2) == -2
    assert multiplying(4,5) == 20
    assert multiplying(1,2,3,4) == 24



   
