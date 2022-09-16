import random

dice = [
    1, 2, 3,
    4, 5, 6
    ]

n_dice = 5
rand_dices = random.choices(dice, k=n_dice)
if rand_dices.count(rand_dices[1]) == n_dice:
    print('Yahtzee')

print(min(rand_dices))
print(max(rand_dices))
rand_dices.sort()
print(rand_dices)
