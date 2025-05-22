from re import S
from src.math_operation import *


def test_add():
    assert add(2,3)==5
    assert add(-1,1)==0 

def test_sub():
    assert substract(3,2)==1
    assert substract(5,2)==3