from random import randint
from Utils import *


# Class representing fighter's attack - it's name, average power of attack, chance to hit
# and cost of energy that takes to perform this attack.
class Attack:
    # initialize method
    def __init__(self, name, average_power, chance_to_hit, energy_cost):
        self.name = name
        self.average_power = average_power
        self.chance_to_hit = chance_to_hit
        self.energy_cost = energy_cost

    # to string method - to be used in terminal run of the game
    def __str__(self):
        return "-->" + "\t" + " " + make_name_same_length(str(self.name), 19, True) \
               + " " + 2 * "\t" + " " + make_name_same_length(str(self.average_power), 19, True) \
               + " " + 4 * "\t" + " " + make_name_same_length(str(self.chance_to_hit), 19, True) \
               + " " + 4 * "\t" + " " + make_name_same_length(str(self.energy_cost), 19, True)

    # returns all the info needed for it to be put into table and to the screen
    def get_info_for_table(self):
        return [self.name, self.average_power, self.chance_to_hit, self.energy_cost]

    # returns actual power of an attack - can differ by 30 percent from average power
    def get_power(self):
        return randint(int(self.average_power * 0.7), int(self.average_power * 1.3))
