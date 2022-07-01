import math


def round_up_or_down(transactions, up=True):
    """Round the list of transactions passed in.
       If up=True (default) round up, else round down.
       Return a new list of rounded values
    """
    num_up = []
    num_down = []
    for num in transactions:
        num_up.append(math.ceil(num))
        num_down.append(math.floor(num))

    if up:
        return num_up
    else:
        return num_down
