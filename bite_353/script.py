
import typer  # use typer.run and typer.Argument

def sum_numbers(a: int, b: int):
    return a + b


def main(a = typer.Argument(), b = typer.Argument()):

    """ CLI that allows you to add two numbers
    """

    print(a + b)


if __name__ == "__main__":
    typer.run(main)