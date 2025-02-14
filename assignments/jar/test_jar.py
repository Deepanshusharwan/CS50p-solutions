from jar import Jar
import pytest

def test_deposit():
    jar = Jar()
    assert str(jar) == ''
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"

def test_withdraw():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.withdraw(1212)
    jar.deposit(9)
    jar.withdraw(2)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪"

def test_init():
    jar = Jar()

def test_capacity():
    jar = Jar()
    assert jar.capacity == 12
    new_jar = Jar(23)
    assert new_jar.capacity == 23

def test_size():
    jar = Jar()
    assert jar.size == 0
    jar.deposit(9)
    assert jar.size == 9

def test_string():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(2)
    assert str(jar) == "🍪🍪"
    jar.withdraw(1)
    assert str(jar) == "🍪"
