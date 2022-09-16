dictionary = {}
new_dictionary = {}

while True:
    key_value = input('Input key/value like this "key;value": ')
    if key_value.lower() == 'revert':
        print(dictionary)
        for key, value in dictionary.items():
            new_dictionary[value] = key
        print(new_dictionary)
        break
    else:
        key_value_split = key_value.split(';')
        dictionary[key_value_split[0]] = key_value_split[1]
