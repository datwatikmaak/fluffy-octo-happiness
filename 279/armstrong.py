def is_armstrong(n: int) -> bool:
    numbers = [int(x) for x in str(n)]
    total = sum(num ** len(numbers) for num in numbers)
    return n == total
