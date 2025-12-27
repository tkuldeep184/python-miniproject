import random

def flip_coin():
    return random.choice(['Heads', 'Tails'])

def roll_die():
    return random.randint(1,6)

def roll_two_dice():
    return (roll_die(), roll_die())