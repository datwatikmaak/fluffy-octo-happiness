from math import floor

num_hundreds = -1


def sum_numbers(numbers: list) -> int:
    """Sums passed in numbers returning the total, also
       update the global variable num_hundreds with the amount
       of times 100 fits in total"""
    global num_hundreds

    if not numbers or sum(numbers) < 100:
        num_hundreds = num_hundreds
    else:
        num_hundreds += floor(sum(numbers) / 100)

    return sum(numbers)
