import pytest
import project
from project import give_hi_back
from project import give_bye_back
from project import give_lol_back

def test_give_hi_back():
    assert give_hi_back(3) == 'hi'
    assert give_hi_back(3) == 'hi'
    assert give_hi_back(4) == 'hi'
    assert give_hi_back(2) == 'hi'
    assert give_hi_back(4) == 'hi'
    assert give_hi_back(5) == 'hi'
    assert give_hi_back(7) == 'hi'
    assert give_hi_back(3) == 'hi'
    assert give_hi_back(5) == 'hi'
    assert give_hi_back(3) == 'hi'
    assert give_hi_back(8) == 'hi'
    assert give_hi_back(9) == 'hi'
    assert give_hi_back(6) == 'hi'
    assert give_hi_back(4) == 'hi'

def test_give_bye_back():
    assert give_bye_back(3) == 'bye'
    assert give_bye_back(4) == 'bye'
    assert give_bye_back(2) == 'bye'
    assert give_bye_back(43) == 'bye'
    assert give_bye_back(7) == 'bye'
    assert give_bye_back(5) == 'bye'

def test_give_lol_back():
    assert give_lol_back(3) == 'lol'
    assert give_lol_back(5) == 'lol'
    assert give_lol_back(9) == 'lol'
    assert give_lol_back(6) == 'lol'
