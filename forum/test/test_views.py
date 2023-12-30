import pytest
from example import Example

@pytest.fixture
def ex():
    return Example()

def test_trivial_double_apple(ex):
    assert ex.trivial_double_apple(5) == 10

def test_trivial_double_apple_zero(ex):
    assert ex.trivial_double_apple(0) == 0

def test_trivial_double_apple_value_exception(ex):
    with pytest.raises(ValueError):
        ex.trivial_double_apple(None)