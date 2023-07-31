from Game.Attack import Attack
from Game.Fighter import Fighter


# method defining fighters and their attacks
def get_heroes():
    voldemort_attacks = [
        Attack('Inferno', 70, 0.7, 40),
        Attack('Avada Kedavra', 500, 0.1, 150),
        Attack('Evil look', 5, 0.9, 5)
    ]

    potter_attacks = [
        Attack('Crucio', 80, 0.75, 40),
        Attack('Avada Kedavra', 500, 0.1, 150),
        Attack('Marbles throw', 10, 0.95, 10)
    ]

    voldemort = Fighter('Voldemort', 99, 200, 180, voldemort_attacks)
    potter = Fighter('Harry Potter', 20, 160, 220, potter_attacks)

    heroes = [voldemort, potter]

    return heroes
