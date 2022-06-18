import string


def remove_punctuation(input_string):
    """Return a str with punctuation chars stripped out"""
    no_punctuation = [char for char in input_string if char not in string.punctuation]
    return "".join(no_punctuation)
