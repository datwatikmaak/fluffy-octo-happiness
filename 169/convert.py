def convert(value: float, fmt: str) -> float:
    """Converts the value to the designated format.

    :param value: The value to be converted must be numeric or raise a TypeError
    :param fmt: String indicating format to convert to
    :return: Float rounded to 4 decimal places after conversion
    """
    if isinstance(value, str):
        raise TypeError

    if fmt == "cm" or fmt == "cm".upper():
        inch = value * (2.54 / 1)
        return round(inch, 4)

    elif fmt == "in":
        cm = value * (1 / 2.54)
        return round(cm, 4)

    else:
        raise ValueError
