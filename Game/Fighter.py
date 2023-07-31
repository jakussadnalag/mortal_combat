from random import randint
from Utils import *
import pywebio.output as out
import pywebio.input as pwinput


# class representing Fighter, its abilities and all the needed info
class Fighter:
    # initialize method
    def __init__(self, name, level, max_health, max_energy, attacks):
        self.name = name
        self.level = level
        self.max_health = max_health
        self.actual_health = max_health
        self.max_energy = max_energy
        self.actual_energy = max_energy
        self.attacks = attacks
        self.min_energy = self.lowest_cost()

    # to string method - for the terminal run of the game
    def __str__(self):
        out.put_text(8 * "--------")
        out.put_text(3 * "\t", make_name_same_length("HEALTH", 15, True), 2 * "\t",
                     make_name_same_length("ENERGY", 15, True))
        out.put_text(make_name_same_length(self.name, 15, True), make_name_same_length(self.actual_health, 7, False),
                     "/", make_name_same_length(self.max_health, 7, True), 2 * "\t",
                     make_name_same_length(self.actual_energy, 7, False), "/",
                     make_name_same_length(self.max_energy, 7, True))
        out.put_text(8 * "--------")
        out.scroll_to(position='bottom')
        return ""

    # returns all the info needed for it to be put into table and to the screen
    def get_info_for_table(self, init):
        health = str(self.max_health)
        energy = str(self.max_energy)
        if not init:
            health = str(self.actual_health) + " / " + str(self.max_health)
            energy = str(self.actual_energy) + " / " + str(self.max_energy)
        return [self.name, health, energy]

    # method for the regeneration of a fighter's energy - adds 10 percent of energy or sets it to the maximum value
    def regenerate(self):
        if self.actual_energy + (self.max_energy * 0.10) < self.max_energy:
            self.actual_energy += (self.max_energy * 0.10)
        else:
            self.actual_energy = self.max_energy
        return self.actual_energy

    # game brake - checks if a fighter was defeated or not by checking on its health
    def is_defeated(self):
        if self.actual_health <= 0:
            out.put_text("Game over!", self.name, "lost! :(")
            return True
        out.scroll_to(position='bottom')
        return False

    # method for outputting table of fighters attacks to the screen
    def print_attacks(self):
        attas = []
        for attack in range(len(self.attacks)):
            atta = [attack] + self.attacks[attack].get_info_for_table()
            attas.append(atta)

        title = "attacks of " + self.name
        out.put_text(("\nHere are the " + title + ":").upper())
        out.put_table([["", "NAME", "AVERAGE POWER", "CHANCE TO HIT", "ENERGY COST"]] + attas)
        out.scroll_to(position='bottom')

    # calculates the actual chance to hit
    def chance_to_hit(self, num_attack):
        chance = []
        for i in range(1, int(self.attacks[num_attack].chance_to_hit * 10)):
            chance.append(i)
        random_num = randint(1, 10)
        return random_num in chance

    # basic game strategy of an attack performed by an artificial player - the computer
    def computer_attack(self, defender, attacker):
        self.print_attacks()
        temp = ["a", "r"]
        what_to_do = temp[randint(0, 1)]
        if what_to_do == "a" or self.actual_energy == self.max_energy:
            num_attack = randint(0, 2)
            while self.actual_energy < self.attacks[num_attack].energy_cost:
                num_attack = randint(0, 2)
            self.actual_energy -= self.attacks[num_attack].energy_cost

            out.put_text(self.name, "used", self.attacks[num_attack].name)
            if Fighter.chance_to_hit(self, num_attack):
                difference = defender.take_damage(num_attack, attacker)
                out.put_text(defender.name, "was hit and lost", difference)
            else:
                list_of_notes = ["was lucky and was not hit.", "dodged the bullet.", "can surely defend. WOW!"]
                out.put_text(defender.name, list_of_notes[randint(0, 2)])
        else:
            self.rest()
        out.scroll_to(position='bottom')

    # method defining output of a player resting for the round - setting its energy to the max value
    def rest(self):
        self.actual_energy = self.max_energy
        out.put_text("You are resting this round. Your energy is on max.")
        out.scroll_to(position='bottom')

    # method for a fighter to surrender by lowering its health to 0 - therefore fighter killing itself
    def surrender(self):
        out.put_text("Poor", self.name, "pooped in own pants and ran.")
        out.scroll_to(position='bottom')
        self.actual_health = 0

    # method that can in 90 percent of the time add 50% of the fighters health and in 10 percent reduce its health by 1%
    def magic_pill(self):
        diarrhea = randint(0, 100)
        if diarrhea <= 90:
            if 1.5 * self.actual_health <= self.max_health:
                self.actual_health = 1.5 * self.actual_health
                out.put_text("Magic pill worked!", self.name, "increased 50% health!")
            else:
                self.actual_health = self.max_health
                out.put_text("Magic pill worked!", self.name, "is 100% healthy now!")
        else:
            self.actual_health = 0.99 * self.actual_health
            out.put_text("Magic pill gave", self.name, "diarrhea and lost 1% health. :( ")
        out.scroll_to(position='bottom')

    # method for the actual attacking. Attacker attacks defender, which can defend the hit or not.
    def attack(self, defender, attacker):
        self.print_attacks()
        out.scroll_to(position='bottom')
        num_attack = pwinput.input("Choose the number of an attack:", type="number")
        while num_attack < 0 or num_attack > 2 \
                or self.actual_energy < self.attacks[num_attack].energy_cost:
            num_attack = pwinput.input("Oh really? You tried. Please, choose another VALID attack:", type="number")

        self.actual_energy -= self.attacks[num_attack].energy_cost

        out.put_text("")
        out.put_text(self.name, " attacked and used", self.attacks[num_attack].name)
        if Fighter.chance_to_hit(self, num_attack) is True:
            difference = defender.take_damage(num_attack, attacker)
            out.put_text(defender.name, "was hit and lost", difference, "health. :(")
        else:
            list_of_notes = ["was lucky and was not hit.", "dodged the bullet.", "can surely defend. WOW!"]
            out.put_text(defender.name, list_of_notes[randint(0, 2)])
        out.put_text("")
        out.scroll_to(position='bottom')

    # this method gives a player/fighter the option to attack, rest, take magic pill or surender.
    def perform_turn(self, defender, attacker):
        if self.actual_energy < self.min_energy:
            thing = pwinput.input("Do you wanna take a magic pill [m], rest [r] or surrender [s]?")
            while thing != "s" and thing != "r" and thing != "m":
                thing = pwinput.input("Do you wanna take a magic pill [m], rest [r] or surrender [s]?")
        else:
            thing = pwinput.input("Do you wanna perform attack[a], "
                                  "take a magic pill [m], rest [r] or surrender [s]?")
            while thing != "a" and thing != "s" and thing != "r" and thing != "m":
                thing = pwinput.input("Do you wanna perform attack[a], "
                                      "take a magic pill[m], rest[r] or surrender[s]?")
        out.put_text("")
        out.scroll_to(position='bottom')

        if thing == "r":
            self.rest()
        elif thing == "s":
            self.surrender()
        elif thing == "m":
            self.magic_pill()
        elif thing == "a":
            self.attack(defender, attacker)

    # calculates the lowest cost of energy needed for an attack
    def lowest_cost(self):
        costs = []
        for attack_i in self.attacks:
            costs.append(attack_i.energy_cost)
        lowest = costs[0]
        for i in costs:
            if i < lowest:
                lowest = i
        return lowest

    # method for taking care of taking damage if the fighter was hit
    def take_damage(self, num_attack, attacker):
        temp = attacker.attacks[num_attack].get_power()
        self.actual_health -= temp
        return temp
