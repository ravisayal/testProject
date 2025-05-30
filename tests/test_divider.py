import pytest
from divider import safe_divide

def test_safe_divide_success():
    assert safe_divide(10, 2) == 5.0

def test_safe_divide_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        safe_divide(1, 0)
