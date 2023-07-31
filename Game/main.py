import random
from heroes import singers, pokemon, harry_potter
from Match import Match
import pywebio.output as out
import pywebio.input as pwinput


# defines basic things for a game to start
def play():
    fighters = fighters_prep()
    duel, game_mode = match_prep(fighters)
    match = Match(duel)
    match.begin(game_mode)


# prepares, initializes and prints out the available fighters
def fighters_prep():
    out.put_text("\nWaking up fighters.\n")
    out.scroll_to(position='bottom')
    fighters = []
    modules = [harry_potter, pokemon, singers]
    for mod in modules:
        for hero in mod.get_heroes():
            fighters.append(hero)

    num_of_fighters = len(fighters)

    if num_of_fighters < 2:
        out.put_text("There are not enough fighters ready. Bye?")
        out.scroll_to(position='bottom')
        return

    out.put_text(str(num_of_fighters) + " of them woke up. Here they are:\n")
    out.scroll_to(position='bottom')

    fights = []
    for fighter in range(len(fighters)):
        fight = [fighter] + fighters[fighter].get_info_for_table(True)
        fights.append(fight)

    out.put_table([["INDEX", "NAME", "HEALTH", "ENERGY"]] + fights)
    out.scroll_to(position='bottom')

    return fighters


# prepares the match by choosing game mode and fighters to fight in a match. After that, a game can start.
def match_prep(fighters):
    duel = []
    num_of_fighters = len(fighters) - 1

    playerA = pwinput.input("Choose index of a fighter number 1 :", type='number')
    while playerA < 0 or playerA > num_of_fighters:
        playerA = pwinput.input("Choose number between 0 and " + num_of_fighters.__str__() + ": ", type='number')
    out.put_text("")
    out.scroll_to(position='bottom')

    game_mode = pwinput.input("Do you wanna play SINGLE PLAYER [s] or MULTIPLAYER [m] ? ")
    while game_mode != "s" and game_mode != "m":
        game_mode = pwinput.input("Type [s] for SINGLE PLAYER or [m] for MULTIPLAYER ? ")
    out.put_text("")
    out.scroll_to(position='bottom')

    if game_mode == "m":
        playerB = pwinput.input("Choose index of a fighter number 2 :", type='number')
        while (playerB < 0 or playerB > num_of_fighters) or (playerA == playerB):
            if playerA == playerB:
                playerB = pwinput.input("Fighter already taken. Choose another fighter :", type='number')
            else:
                playerB = pwinput.input("Choose number between 0 and " + num_of_fighters.__str__() + ":", type='number')
        out.put_text("")
        out.scroll_to(position='bottom')
    else:
        playerB = random.randint(0, num_of_fighters)
        while playerA == playerB:
            playerB = random.randint(0, num_of_fighters)

    duel.append(fighters[playerA])
    duel.append(fighters[playerB])

    out.put_text("\nFighter number one:", duel[0].name)
    out.put_text("Fighter number two:", duel[1].name)
    out.put_text("GAME STARTS NOW. FIGHT!")
    out.put_text(5 * "=======" + "\n")
    out.scroll_to(position='bottom')

    return duel, game_mode


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    play()
