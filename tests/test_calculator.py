import pytest
from src.calculator import *

@pytest.mark.smoke
def test_add():
    assert add(2,3) == 5

@pytest.mark.extended
def test_add_raises_type_error_on_string_input():
    with pytest.raises(TypeError):
        add(5, "hello")

@pytest.mark.extended
def test_divide_by_zero_with_exc_error_with_msg():
    with pytest.raises(ValueError) as excinfo:
        divide(10,0)

    assert "Нельзя делить на ноль" in str(excinfo.value)

@pytest.mark.extended
@pytest.mark.skip(reason="тест устарел")
def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10,0)

@pytest.mark.skip(reason="Эта функциональность будет реализована в версии 2.0")
def test_subtraction():
    """Тест для будущей функции вычитания."""
    # assert subtract(10, 5) == 5
    pass