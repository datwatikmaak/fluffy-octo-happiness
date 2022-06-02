from collections import deque


def rotate(string, n):
    """Rotate characters in a string.
    Expects string and n (int) for number of characters to move.
    """
    d = deque(list(string))
    d.rotate(-n)
    return "".join(d)
