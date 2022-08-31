from typing import Iterator


class Vehicle:

    def __init__(self, vehicle_type: str, brand: str, model: str, production_year: str, millage: str):
        self.vehicle_type = vehicle_type
        self.brand = brand
        self.model = model
        self.production_year = production_year
        self.millage = millage

    def transfer_data(self) -> dict:
        '''
        It's used to return vehicle data in dict
        :return: dict of vehicle data
        '''
        return {"vehicle_type": self.vehicle_type, "brand": self.brand, "model": self.model,
                "production_year": self.production_year, "millage": self.millage}


class AuctionPosition:
    """
    Makes a AuctionPosition object to create a listing
    """

    def __init__(self, generator: Iterator, vehicle: dict, current_price: str = "20000", current_winner: str = ""):
        self.id = str(generator.__next__())
        self.vehicle = vehicle
        self.current_price = current_price
        self.current_winner = current_winner

    def transfer_data(self):
        """
        It's used to return auction data in dict
        :return: dict of auction data
        """
        return {"id": self.id, "vehicle": self.vehicle, " current_price": self.current_price,
                "current_winner": self.current_winner}

    def display_data(self):
        defaults = dict(id=4, vehicle_type=9, brand=10, model=15, production_year=4, millage=7, current_price=13,
                        current_winner=15)

        def ready_module(default_name, subject) -> str:
            """
            Makes final action outcome elements more standardized 
            :param default_name: name of key inside dict with default module length
            :param subject:  value of property
            :return:
            """
            spaces = defaults[default_name] - len(subject)
            return f"{subject}{' ' * spaces}"

        v = self.vehicle
        print(f"|{ready_module('id', self.id)}"
              f"{ready_module('vehicle_type', v['vehicle_type'])}|"
              f"{ready_module('brand', v['brand'])}|"
              f"{ready_module('model', v['model'])}|"
              f"{ready_module('production_year', v['production_year'])}|"
              f"{ready_module('millage', v['millage'])}|"
              f"{ready_module('current_price', self.current_price)}|"
              f"{ready_module('current_winner', self.current_winner)}|")

    def new_bid(self, new_price: str, new_winner: str) -> None:
        """
        Updates data about new price and new winner when bid is made and correct
        :param new_price:  new current price of auction position
        :param new_winner:  new current winner of auction position
        :return: 
        """
        self.current_price = new_price
        self.current_winner = new_winner

 