import itertools


def running_mean(sequence):
    """Calculate the running mean of the sequence passed in,
       returns a sequence of same length with the averages.
       You can assume all items in sequence are numeric."""
    averages = list(itertools.starmap(
        lambda a, b: b / a,
        enumerate(itertools.accumulate(sequence), 1))
    )
    return [round(num, 2) for num in averages]
