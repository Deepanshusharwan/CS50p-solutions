
import plates
from plates import is_valid


def test_beginning_alphabet_is_valid():
    assert is_valid("as848")
    assert is_valid("39ji") == False
    assert is_valid("AA")
    assert is_valid("A2") == False


def len_is_valid():
    assert plates.is_valid("h") == False
    assert plates.is_valid("hihfihiihihihih") == False
    assert plates.is_valid('') == False
    assert plates.is_valid("") == False
    assert plates.is_valid("himan")
    assert is_valid("ABC123")
    assert is_valid("ABC12")
    assert is_valid("ABC1")
    assert is_valid("ABC")
    assert is_valid("A") == False
    assert is_valid("ABCD123") == False
    assert is_valid("ABCDE123") == False


def number_position_is_valid():
    assert is_valid("he88")
    assert is_valid("he88m") == False


def zero_placement_is_valid():
    assert is_valid("hij0") == False
    assert is_valid("hiw930")
    assert is_valid("hi00") == False


def test_only_alphas():
    assert is_valid("ABC123")
    assert is_valid("AB12")
    assert is_valid("AB")
    assert is_valid("$1") == False
    assert is_valid("1$") == False
    assert is_valid("12$") == False
    assert is_valid("  AB") == False
    assert is_valid("!?AB2*") == False
    assert is_valid("*:") == False
    assert is_valid("B>") == False


def test_number_order():
    assert is_valid("ABC123")
    assert is_valid("AB12")
    assert is_valid("AB12C") == False
    assert is_valid("AB1C") == False


def test_two_letters():
    assert is_valid("ABC123")
    assert is_valid("AB12")
    assert is_valid("A12") == False
    assert is_valid("1234") == False


def test_first_number_not_zero():
    assert is_valid("ABC123")
    assert is_valid("AB12")
    assert is_valid("AB0") == False
    assert is_valid("ABC01") == False


def test_length():
    assert is_valid("ABC123")
    assert is_valid("ABC12")
    assert is_valid("ABC1")
    assert is_valid("ABC")
    assert is_valid("A") == False
    assert is_valid("ABCD123") == False
    assert is_valid("ABCDE123") == False


def test_alphanumeric():
    assert is_valid("hi43")
    assert is_valid("hion")
    assert is_valid("kjo,.k") == False
