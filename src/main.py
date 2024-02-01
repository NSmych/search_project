from get_token import get_token
from cli import cli


def main_function():
    get_token()
    print("This is the main function and it had run.")
    cli()


if __name__ == "__main__":
    main_function()
