from twttr import shorten


def test_lowercase_shorten():
    assert shorten("twitter") == "twttr"
    assert shorten("buddy") == "bddy"


def test_uppercase_shorten():
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("BUDDY") == "BDDY"

def test_numbers_shorten():
    assert shorten("cs50e") == "cs50"
    assert shorten("Pure35") == "Pr35"

def test_punctuation_shorten():
    assert shorten("hey,.:uip") == "hy,.:p"
    assert shorten("ui,./';.,;/';.,") == ",./';.,;/';.,"


