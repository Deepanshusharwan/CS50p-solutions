
from um import count

def test_count():
    assert count("hi my name is um yummy") == 1
    assert count("Um") == 1
    assert count("um..well that is bad") == 1
