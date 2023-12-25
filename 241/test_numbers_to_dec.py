import pytest
import random

from numbers_to_dec import list_to_decimal



def test_value_error_1():

    numbers = [-1,5,1,1]
    
    with pytest.raises(ValueError) as e:
        list_to_decimal(numbers)

            

def test_value_error_2():
    numbers = [5,9,12]
    
    with pytest.raises(ValueError) as e:
        list_to_decimal(numbers)

def test_value_error_3():
    numbers = [5,-1,9,14]
    
    with pytest.raises(ValueError) as e:
        list_to_decimal(numbers)

def test_type_error():

    values = [2.5,2,1]

    with pytest.raises(TypeError) as e:
        list_to_decimal(values)


def test_type_error_mixed():

    values = [2.5,2,1,"hello"]

    with pytest.raises(TypeError) as e:
        list_to_decimal(values)

def test_1():


    assert list_to_decimal([1,2,3]) == 123


def test_2():


    assert list_to_decimal([0,5,2,2,3]) == 5223



