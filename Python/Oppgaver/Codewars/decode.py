import math


def decode(deck):

    alphabet = [
            ' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
            'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
        ]

    cards = [
        'AC', '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', 'TC', 'JC', 'QC', 'KC',
        'AD', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', 'TD', 'JD', 'QD', 'KD',
        'AH', '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', 'TH', 'JH', 'QH', 'KH',
        'AS', '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', 'TS', 'JS', 'QS', 'KS'
        ]

    permutation = 0
    tracker = 0
    counter = 0
    while True:
        if len(cards) == 0:
            break
        if cards[counter] == deck[tracker]:
            cards.pop(counter)
            counter = 0
            tracker += 1
        else:
            permutation += math.factorial(len(cards) - 1)
            counter += 1

    decoded_string = []
    n = 26

    while True:
        if n == 0:
            break
        base = 27 ** (n - 1)
        index = int(permutation/base)
        decoded_string.append(index)
        permutation -= index * base
        n -= 1

    final_string = []
    for i in decoded_string:
        final_string.append(alphabet[i])
    final_string_join = ''.join(final_string)
    output = final_string_join.strip()
    return output


received_deck = [
    "AC", "2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "TC", "JC", "QC", "KC",
    "AD", "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "TD", "JD", "QD", "KD",
    "AH", "2H", "3H", "4H", "8H", "9S", "3S", "2S", "8S", "TS", "QS", "9H", "7H",
    "KH", "AS", "JH", "4S", "KS", "JS", "5S", "TH", "7S", "6S", "5H", "QH", "6H"
    ]

decoded = decode(received_deck)
print(decoded)
