from functools import partial


def rounding(n, r):
    return round(r, n)


# create 2 partials:
# - 'rounder_int' rounds to int (0 places)
# - 'rounder_detailed' rounds to 4 places
rounder_int = partial(rounding, 0)
rounder_detailed = partial(rounding, 4)
