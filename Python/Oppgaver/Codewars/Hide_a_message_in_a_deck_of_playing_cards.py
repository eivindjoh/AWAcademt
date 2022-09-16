import math

# n er antall kort
# k er hvilken permutasjon

text = "JAY FLOH LIKER PYTHON"


def encode(text_input):
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

    # Find base 27
    sequence = []
    for i in text_input:
        alphabet_index = alphabet.index(i)
        sequence.append(alphabet_index)
    code_length = len(sequence)
    base_27 = 0
    for count, x in enumerate(sequence):
        number = x * (27 ** (code_length - count - 1))
        base_27 += number

    # Find card sequence
    answer = []
    n = len(cards)
    k = base_27
    for a in range(n):
        index = int(k/math.factorial(n - 1))
        '''if k % math.factorial(n - 1) == 0:
            index -= 1'''
        pop_index = cards.pop(index)
        answer.append(pop_index)
        k = k - math.factorial(n - 1) * index
        n -= 1
    return answer


deck = encode(text)
print(deck[0:13])
print(deck[13:26])
print(deck[26:39])
print(deck[39:52])


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
    'AC', '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', 'TC', 'JC', 'QC', 'KC',
    'AD', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', 'TD', 'QD', 'TH', '4H',
    '4S', '8H', '3S', 'AS', 'KH', 'JD', 'KS', '8S', '7S', '5H', 'QS', '6H', 'JH',
    'AH', '2H', 'KD', '3H', '5S', '2S', '7H', '9H', '6S', '9S', 'TS', 'QH', 'JS'
]

decoded = decode(received_deck)
print(decoded)
