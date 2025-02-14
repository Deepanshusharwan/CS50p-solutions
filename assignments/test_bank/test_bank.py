from bank import value

def test_20_value():
    assert value("hey how is it going") == 20
    assert value("hi how is your day going?") == 20


def test_0_value():
    assert value("hello good evening") == 0
    assert value("helloo sir") == 0


def test_100_value():
    assert value("good morning mam") == 100
    assert value("welcome") == 100


def test_case_insesitivity_value():
    assert value("Hello Sire") == 0
