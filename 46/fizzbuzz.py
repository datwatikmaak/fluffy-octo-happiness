from typing import Union


def fizzbuzz(num: int) -> Union[str, int]:
    if num % 5 == 0 and num % 3 == 0:
        return "fizzbuzz"
    elif num % 5 == 0:
        return "buzz"
    elif num % 3 == 0:
        return "fizz"
    else:
        return num
