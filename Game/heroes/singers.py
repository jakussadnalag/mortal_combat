from Game.Attack import Attack
from Game.Fighter import Fighter


# method defining fighters and their attacks
def get_heroes():
    cyrus_attacks = [
        Attack("Wrecking ball", 100, 0.5, 70),
        Attack("Hammer lick", 45, 0.7, 40),
        Attack("Blonde shine", 20, 0.9, 20)
    ]

    bieber_attacks = [
        Attack("Whoa-ouu", 15, 0.95, 5),
        Attack("Baby ohh", 99, 0.4, 90),
        Attack("Drum solo", 35, 0.7, 25)
    ]

    cyrus = Fighter("Miley Cyrus", 28, 140, 200, cyrus_attacks)
    bieber = Fighter("Justin Bieber", 26, 190, 150, bieber_attacks)

    heroes = [cyrus, bieber]

    return heroes
