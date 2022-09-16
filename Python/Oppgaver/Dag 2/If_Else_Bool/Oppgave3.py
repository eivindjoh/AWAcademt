import random

def roll_dices():
    dice_list = []
    dice_eyes = [
        1,2,3,
        4,5,6
        ]
    for i in range(5):
        dice_list.append(random.choice(dice_eyes))
    return dice_list

count_throws = 0

while True:
    roll = roll_dices()
    count_throws += 1
    print(list(roll))
    if roll.count(roll[0]) == 5:
        print(f'Yatzee!!! In {count_throws} throws')
        exit()
