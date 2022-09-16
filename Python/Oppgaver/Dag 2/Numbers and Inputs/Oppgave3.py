bar_length = 10
current_number = 80
total_numb = 100
steps = int((current_number/total_numb) * bar_length)
count_of_like = steps * '='
count_of_spaces = (bar_length - steps) * ' '
print(f'\r|{count_of_like}>{count_of_spaces}|')
