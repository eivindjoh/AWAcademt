values = [3, 13, 21, 20, 5, 9, 2, 4]
alpha = 0.45
values.sort()
lower_idx = round(len(values)*(alpha/2))
upper_idx = round(len(values)*(1-(alpha/2))-1)
print(f'lower_index: {lower_idx}')
print(f'upper_index: {upper_idx}')
print(f'lower_value: {values[lower_idx]}')
print(f'upper_value: {values[upper_idx]}')
