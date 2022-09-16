def score(dice):
    counter = {}
    points = 0

    for i in dice:
        if i not in counter:
            counter[i] = 1
        else:
            counter[i] += 1

    jackpot = [key for key, value in counter.items() if value >= 3]

    if not jackpot:
        pass
    elif jackpot[0] == 1:
        points += jackpot[0]*1000
        counter[jackpot[0]] -= 3
    else:
        points += jackpot[0]*100
        counter[jackpot[0]] -= 3

    for key, value in counter.items():
        if key == 1:
            points += value * 100
        elif key == 5:
            points += value * 50
        else:
            continue
    return points


output = score([2, 3, 4, 6, 2])
print(output)