import pywebio.output as out


# class defining the whole match with rounds and fighters
class Match:
    # initialize method
    def __init__(self, fighters):
        self.rounds = 1
        self.fighters = list(fighters)
        if self.fighters[0].level > self.fighters[1].level:
            self.attacker = self.fighters[0]
            self.defender = self.fighters[1]
        else:
            self.attacker = self.fighters[1]
            self.defender = self.fighters[0]

    # to string method outputting the table of currently playing fighters.
    def __str__(self):
        fights = []
        for fighter in range(len(self.fighters)):
            fight = self.fighters[fighter].get_info_for_table(False)
            fights.append(fight)

        out.put_table([["", "HEALTH", "ENERGY"]] + fights)
        out.scroll_to(position='bottom')

    # increments the round of the game by one
    def inc_rounds(self):
        self.rounds += 1

    # outputs the general info of the round
    def print_round_stuff(self):
        out.put_text("\n" + 5 * "+++++" + "\n")
        out.put_text("ROUND NUMBER ", self.rounds)
        out.put_text(self.attacker.name + ", it's your turn!")
        out.put_text("Here's some info about the fighters: \n")
        self.__str__()
        out.scroll_to(position='bottom')

    # defining what happens after the game begins until the end of the game depending on a game mode
    def begin(self, game_mode):
        if game_mode == "s":
            while not self.defender.is_defeated():
                self.print_round_stuff()
                self.inc_rounds()
                self.defender.regenerate()
                if self.fighters[1] == self.defender:
                    self.perform_round()
                else:
                    self.attacker.computer_attack(self.defender, self.attacker)
                if self.defender.is_defeated():
                    break
                self.switch()
        elif game_mode == "m":
            while not self.defender.is_defeated():
                self.print_round_stuff()
                self.inc_rounds()
                self.defender.regenerate()
                self.perform_round()
                if self.defender.is_defeated():
                    break
                self.switch()

    # method for switching attacker and defender
    def switch(self):
        if self.attacker == self.fighters[0]:
            self.attacker = self.fighters[1]
            self.defender = self.fighters[0]
        else:
            self.attacker = self.fighters[0]
            self.defender = self.fighters[1]

    # make fighters to perform a round
    def perform_round(self):
        self.attacker.perform_turn(self.defender, self.attacker)
