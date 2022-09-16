month_short = input('Month 3 characters: ').lower()

short = [
    'jan','feb','mar','apr',
    'may','jun','jul','aug',
    'sep','oct','nov','dec'
    ]
long = [
    'january','february','march', 'april',
    'may','june','july','august',
    'september','october','november','december'
    ]

for count, month in enumerate(short):
    if month == month_short:
        print(long[count].capitalize())
        break

if month_short not in short:
    print('Unknown')
