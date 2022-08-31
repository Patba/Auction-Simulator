from objects import AuctionPosition
from utils import header
from random import randint
from simulators import bid_simulator
from utils import id_generator, bidder_generator, create_cars
from time import sleep


def main() -> None:
    id_gen = id_generator(100)

    #a list of vehicles to auction
    vehicle_li = [
        {"vehicle_type": "sedan", "brand": "bmw", "model": "m5",
         "production_year": "2005", "millage": "180000"},
        {"vehicle_type": "coupe", "brand": "mercedes", "model": "AMG S63",
         "production_year": "2003", "millage": "190000"},
        {"vehicle_type": "SUV", "brand": "mercedes", "model": "AMG G63",
         "production_year": "2005", "millage": "300000"},
        {"vehicle_type": "sedan", "brand": "bmw", "model": "m3", "production_year": "2005",
         "millage": "200000"}
    ]
    
    cars = create_cars(vehicle_li)
    auction_positions = [AuctionPosition(id_gen, car.transfer_data()) for car in cars]

    for auction in auction_positions:
        sleep(1)
        bidens = bidder_generator(20, 15000, 100000)
        auction.new_bid(*bid_simulator(bidens, str(randint(10000, 20000))))

    header()
    for auction in auction_positions:
        auction.display_data()


if __name__ == '__main__':
    main()
