
from numb3rs import validate
import sys


def test_greater_value():
    assert validate("234.2345.23.4") == False
    assert validate("2938.2983.2938.2938") == False
    assert validate("123.4321.32.2") == False
    assert validate('127.300.1.2') == False
    assert validate('127.1.300.2') == False
    assert validate('127.1.2.300') == False
    assert validate('127.300.300.300') == False


def test_lesser_value():
    assert validate("-2.3.23.23") == False
    assert validate("-1.3.2.32") == False


def test_true_value():
    assert validate("33.23.123.33") == True
    assert validate("23.23.12.255") == True
