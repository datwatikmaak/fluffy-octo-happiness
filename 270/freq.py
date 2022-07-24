from collections import Counter


def freq_digit(num: int) -> int:
    numbers = [int(x) for x in str(num)]
    return Counter(numbers).most_common(2)[0][0]
