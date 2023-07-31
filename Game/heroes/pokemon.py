from Game.Attack import Attack
from Game.Fighter import Fighter


# method defining fighters and their attacks
def get_heroes():
    pikachu_attacks = [
        Attack('Tail slash', 15, 0.9, 5),
        Attack('Static field', 60, 0.8, 35),
        Attack('Lighting bolt', 110, 0.4, 60)
    ]

    charmander_attacks = [
        Attack('Ember', 10, 0.95, 8),
        Attack('Flame burst', 55, 0.75, 30),
        Attack('Flame thrower', 130, 0.3, 80)
    ]

    pikachu = Fighter('Pikachu', 42, 200, 120, pikachu_attacks)
    charmander = Fighter('Charmander', 40, 190, 150, charmander_attacks)

    heroes = [pikachu, charmander]

    return heroes
