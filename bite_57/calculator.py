import argparse

def calculator(operation: str, numbers: list):
    """TODO 1:
       Create a calculator that takes an operation and list of numbers.
       Perform the operation returning the result rounded to 2 decimals"""
    if operation == 'add':
        return round(sum(numbers), 2)
    elif operation == 'sub':
        return round(numbers[0] - sum(numbers[1:]), 2)
    elif operation == 'mul':
        result = 1
        for number in numbers:
            result *= number
        return round(result, 2)
    elif operation == 'div':
        result = numbers[0]
        for number in numbers[1:]:
            result /= number
        return round(result, 2)


def create_parser():
    """TODO 2:
       Create an ArgumentParser object:
       - have one operation argument,
       - have one or more integers that can be operated on.
       Returns a argparse.ArgumentParser object.

       Note that type=float times out here so do the casting in the calculator
       function above!"""
    parser = argparse.ArgumentParser(description='A simple calculator')

    parser.add_argument('-a', '--add', nargs='+', type=float, help='Sums numbers')
    parser.add_argument('-s', '--sub', nargs='+', type=float, help='Subtracts numbers')
    parser.add_argument('-m', '--mul', nargs='+', type=float, help='Multiplies numbers')
    parser.add_argument('-d', '--div', nargs='+', type=float, help='Divides numbers')
    return parser

def call_calculator(args=None, stdout=False):
    """Provided/done:
       Calls calculator with provided args object.
       If args are not provided get them via create_parser,
       if stdout is True print the result"""
    parser = create_parser()

    if args is None:
        args = parser.parse_args()

    # taking the first operation in args namespace
    # if combo, e.g. -a and -s, take the first one
    for operation, numbers in vars(args).items():
        if numbers is None:
            continue

        try:
            res = calculator(operation, numbers)
        except ZeroDivisionError:
            res = 0

        if stdout:
            print(res)

        return res


if __name__ == '__main__':
    call_calculator(stdout=True)