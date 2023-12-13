import pytest
import MathProblem
from MathProblem import add_num, multiply_num, divide_num, combine_results


# Unit Tests for add_num
def test_add_num_1():                           #all unit test functions should be named beginning with "test"
    retvalue = add_num(2, 5)           
    assert retvalue == 7    

def test_add_num_2():         
    retvalue = add_num(-2, -5)           
    assert retvalue == -7           

def test_add_num_3():         
    retvalue = add_num(-0.5, 2.5)           
    assert retvalue == 2.0
                

# Unit Tests for multiply_num
def test_multiply_num_1():
    retvalue = multiply_num(1, 3, 6)
    assert retvalue == 18  

def test_multiply_num_2():
    retvalue = multiply_num("1", "3", "6")
    assert retvalue == 18   

def test_multiply_num_3():
    retvalue = multiply_num(int("1"), int("3"), int("6"))
    assert retvalue == 18               

def test_multiply_num_3():
    retvalue = multiply_num([1], [3], [6])
    assert retvalue == 18 

def test_multiply_num_4():
    retvalue = multiply_num(0.5, 3.2, 6)
    assert retvalue == 9.6          

def test_multiply_num_5():
    retvalue = multiply_num(-1, -0.5, -3.2)
    assert retvalue == -1.6


# Unit Tests for divide_num
def test_divide_num_1():
    retvalue = divide_num(0, 1)
    assert retvalue == 0

def test_divide_num_2():
    retvalue = divide_num(1, 0)
    assert retvalue == "ERROR: CANNOT DIVIDE BY ZERO"

def test_divide_num_3():
    retvalue = divide_num(1, 3)
    assert retvalue == 0.3333

def test_divide_num_4():
    retvalue = divide_num(1.5, 2)
    assert retvalue == 0.75

def test_divide_num_5():
    retvalue = divide_num(NULL, 5)
    assert retvalue == "ERROR: MISSING INPUT VALUE"


# Unit Tests for combine_results
def test_combine_results_1():
    retvalue = combine_results(1, 2, 3)
    assert retvalue == 0.6666

def test_combine_results_2():
    retvalue = combine_results(4, 0.5, 2)
    assert retvalue == 1.5

def test_combine_results_3():
    retvalue = combine_results(1, 4, 0)
    assert retvalue == error

