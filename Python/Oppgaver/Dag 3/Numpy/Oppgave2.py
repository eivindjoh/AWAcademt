#a
captured = (
    'Pikachu', 'Pidgey', 'Abra',
    'Pidgey', 'Eevee', 'Pidgey'
    )

#b
'''Hvis vi bare ønsker å se rekkefølgen pokemon'ene har blitt fanget
i kan vi bruke en tuple da vi ikke kan forandre på elementene, men 
skulle vi ha endret på dette måtte vi ha brukt en liste.'''

#c
captured_pidgeys = captured.count('Pidgey')
print(captured_pidgeys)

#d
pokemon = input('Choose pokemon: ')

if pokemon in captured:
    pokemon_captured = 'Yes'
else:
    pokemon_captured = 'No'

number_of_pokemon = len(captured)
unique_pokemon = len(set(captured))

print(f'Pokemon captured?: {pokemon_captured}')
print(f'Total of captured pokemon: {number_of_pokemon}')
print(f'Total of unique pokemon captured: {unique_pokemon}')
