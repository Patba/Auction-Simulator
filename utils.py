from typing import Iterator, List
from random import randint
from objects import Vehicle


class TermColors:
    """
    Sets variables to change console's color output
    """
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def id_generator(size: int) -> Iterator:
    """
    Creates iterable object, that generates new id values one by one to avoid overload of memory
    :param size:  number of highest id available
    :return: iterator object
    """
    for i in range(1, size):
        yield i


def header() -> None:
    """
    creates a header in a summary
    :return:
    """
    defaults = {"id": 4, "vehicle_type": 9, "brand": 10, "model": 15,
                "production_year": 4, "millage": 7, "current_price": 13, "current_winner": 15}

    def ready_module(default_name, subject) -> str:
        """

        :param default_name:
        :param subject:
        :return:
        """
        spaces = defaults[default_name] - len(subject)
        return f"{subject}{' ' * spaces}"

    print(f"|{ready_module('id', 'id')}"
          f"{ready_module('vehicle_type', 'type')}|"
          f"{ready_module('brand', 'brand')}|"
          f"{ready_module('model', 'model')}|"
          f"{ready_module('production_year', 'year')}|"
          f"{ready_module('millage', 'millage')}|"
          f"{ready_module('current_price', 'current price')}|"
          f"{ready_module('current_winner', 'current winner')}")
    print(" ")


def bidder_generator(amount: int, min_cash: int, max_cash: int) -> dict:
    """
    Generates bidders
    :param amount: of bidders
    :param min_cash: min cash of bidders
    :param max_cash: max cash of bidders
    :return:
    """
    customers = {}
    for i in range(amount):
        customers[i] = randint(min_cash, max_cash)
    return customers


def create_cars(cars_li: List[dict]) -> list:
    """
    Creates list of Vehicle class instances
    :param cars_li: list of dicts that have car properties data
    :return: list
    """
    return [Vehicle(**car) for car in cars_li]
