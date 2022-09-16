def my_sum(x, y):
    return x + y

def my_subtract(x, y):
    return x - y

def my_multiply(x, y):
    return x * y

def my_divide(x, y):
    return x / y

try:
    first_number = float(input('First number: '))
except ValueError:
    print('Du må føre inn et tall')
    exit()

operator = input(r'Operator (+,-,/,*): ')
if operator not in ['+', '-', r'/', '*']:
    print('Velg riktig operator')
    exit()

try:
    second_number = float(input('Second number: '))
except ValueError:
    print('Du må føre inn et tall')
    exit()

if operator == r'/' and second_number == 0:
    print('Du kan ikke dele på 0')
    exit()

if operator == '+':
    print(my_sum(first_number, second_number))
elif operator == '-':
    print(my_subtract(first_number, second_number))
elif operator == '*':
    print(my_multiply(first_number, second_number))
elif operator == r'/':
    print(my_divide(first_number, second_number))
