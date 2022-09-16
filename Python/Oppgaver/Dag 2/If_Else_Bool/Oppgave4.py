bar_length = 100
current_number = 50
total_numb = 100
steps = int((current_number/total_numb) * bar_length)
count_of_like = steps * '='
count_of_spaces = (bar_length - steps) * ' '
if current_number/total_numb == 1:
    print(f'|{count_of_like}{count_of_spaces}|')
else:
    print(f'|{count_of_like}>{count_of_spaces}|')