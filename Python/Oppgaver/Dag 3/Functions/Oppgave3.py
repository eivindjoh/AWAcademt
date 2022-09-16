def my_calculator(x: float, operators: str, y: float) -> float:
    """
    Math

    :param x: float
    :param operators: str
    :param y: float
    :return: float
    """
    if operators == '+':
        return x + y

    if operators == '-':
        return x - y

    if operators == '*':
        return x * y

    if operators == '/':
        return x / y


try:
    first_number = float(input('First number: '))
except ValueError:
    print('Du må føre inn et tall')
    exit()

operator = input(r'Operator (+,-,/,*): ')
if operator not in ['+', '-', '/', '*']:
    print('Velg riktig operator')
    exit()

try:
    second_number = float(input('Second number: '))
except ValueError:
    print('Du må føre inn et tall')
    exit()

if operator == '/' and second_number == 0:
    print('Du kan ikke dele på 0')
    exit()

print(my_calculator(first_number, operator, second_number))
