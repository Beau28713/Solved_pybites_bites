import typer  # use typer.run and typer.Argument

def sum_numbers(a: int, b: int):
    """ CLI that allows you to add two numbers
        The value of the first summand
        The value of the second summand
    """
    return a + b


def main(a = typer.Argument(default=...), b = typer.Argument(default=...)):
    
    return sum_numbers(a, b)


if __name__ == "__main__":
    typer.run(main)