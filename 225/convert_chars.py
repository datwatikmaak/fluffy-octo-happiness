PYBITES = "pybites"


def convert_pybites_chars(text):
    """Swap case all characters in the word pybites for the given text.
       Return the resulting string."""
    result = ""
    for char in text:
        if char in PYBITES.upper() and char.isupper():
            result += char.lower()
        elif char in PYBITES.lower() and char.islower():
            result += char.upper()
        else:
            result += char

    return result
