import re
from decimal import Decimal


def generator_numbers(text):
    pattern = r"\d+\.\d+"
    numbers = re.finditer(pattern, text)

    for number in numbers:
        yield Decimal(number.group())


def sum_profit(text, func):
    # return sum(func(text))
    total = 0

    for income in func(text):
        total += income

    return total


def main():
    text = """
        The employee's total income consists of several parts: 1000.01 as the main income, 
        supplemented by additional receipts of 27.45 and 324.00 dollars.
        """
    total_income = sum_profit(text, generator_numbers)
    print(f"Total income: {total_income}")


if __name__ == "__main__":
    main()
