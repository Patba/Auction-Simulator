from typing import Tuple
from time import sleep
from utils import TermColors


def bid_simulator(bidders: dict, veh_price: str) -> Tuple[str, str]:
    """
    Simulates a bidding between bidders
    :param bidders: bidders
    :param veh_price: initial bid
    :return:
    """
    highest_bidder = None

    if_out = []
    veh_price = float(veh_price)

    def decision(probability):
        """
        It's used to calculate True or False based on chance of a bid
        :param probability: 
        :return:
        """
        import random
        return random.random() < probability


    while len(if_out) <= (len(bidders.keys()) - 1):

        veh_price_temp = veh_price + (veh_price * 0.20) #bids the price by 20%

        for bidder, balance in bidders.items():
            if bidder not in if_out:
                if veh_price_temp > balance: #if the future bid price is higher than the balance then bidder is out
                    if_out.append(bidder)
                if veh_price_temp < balance:
                    chance_to_bid = round(((balance - veh_price) / (balance / 100)) / 100, 1) #chance to bid
                    if chance_to_bid > 100: #if the bid chance is higher than 100 then it should equal 100
                        chance_to_bid = 100

                    if_bid = decision(chance_to_bid) #makes a decision based on chance_to_bid

                    print(f"{TermColors.ENDC}Decision by bidder no. {bidder} made for {if_bid}, by being sure of that by {chance_to_bid}")

                    if if_bid:
                        if veh_price_temp < balance:
                            veh_price = veh_price_temp
                            highest_bidder = bidder
                            sleep(0.01)
                            print(f"{TermColors.OKGREEN}New Price by bidder no. {bidder} equals {veh_price}")
                    sleep(0.05)
                    print(f"{TermColors.ENDC}No bet was made by bidder no. {bidder}, car stays at {veh_price}")

    print(f"{TermColors.OKCYAN}Highest bid by {highest_bidder} for {veh_price}")
    sleep(2)
    return str(round(veh_price, 2)), str(highest_bidder)
