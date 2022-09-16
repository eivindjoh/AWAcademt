def move_zeros(lst):
    numbers = []
    zeros = []
    for i in lst:
        if i == 0:
            zeros.append(i)
        else:
            numbers.append(i)
    return numbers + zeros


liste = [1, 2, 0, 1, 0, 1, 0, 3, 0, 1]
ny_liste = move_zeros(liste)
print(ny_liste)