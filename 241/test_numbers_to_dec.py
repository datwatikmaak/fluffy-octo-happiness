import pytest

from numbers_to_dec import list_to_decimal


@pytest.mark.parametrize("good_input, expected", [
    ([0, 4, 2, 8], 428),
    ([1, 2], 12),
    ([3], 3),
])
def test_numbers_to_dec_good(good_input, expected):
    assert list_to_decimal(good_input) == expected


@pytest.mark.parametrize("value_error_input", [
    [-3, 12],
    [3, 10],
])
def test_numbers_to_dec_value_error(value_error_input):
    with pytest.raises(ValueError):
        list_to_decimal(value_error_input)


@pytest.mark.parametrize("type_error_input", [
    [6, 2, True],
    [3.6, 4, 1],
    ['4', 5, 3, 1],
])
def test_numbers_to_dec_value_error(type_error_input):
    with pytest.raises(TypeError):
        list_to_decimal(type_error_input)
