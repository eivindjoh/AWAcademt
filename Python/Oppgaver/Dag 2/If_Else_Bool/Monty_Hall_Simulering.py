import random

repetitions = 100000

print('Monty Hall Test:\n')

count_win = 0
count_fail = 0

for i in range(repetitions):
    doors = ['a', 'b', 'c']
    fact = random.choice(doors)
    choice = random.choice(doors)
    if choice == fact:
        count_fail += 1
    else:
        count_win += 1

print(f' Changing choice:')
print(f' wins = {count_win}')
print(f' fails = {count_fail}')
print(f' win% = {round(((count_win/repetitions) * 100), 2)}%\n')

count_win = 0
count_fail = 0

for i in range(repetitions):
    doors = ['a', 'b', 'c']
    fact = random.choice(doors)
    choice = random.choice(doors)
    if choice == fact:
        count_win += 1
    else:
        count_fail += 1

print(f' Not changing choice:')
print(f' wins = {count_win}')
print(f' fails = {count_fail}')
print(f' win% = {round(((count_win/repetitions) * 100), 2)}%')
