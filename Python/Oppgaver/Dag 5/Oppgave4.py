def set_by_path(input_dict, path, value):

    new_dict = input_dict
    reverse_path = path[::-1]
    list_dict = {}

    for i in range(len(reverse_path)):
        if i == 0:
            list_dict = {reverse_path[0]: value}
        else:
            list_dict = {reverse_path[i]: list_dict}

    key = list(list_dict.keys())
    value = list(list_dict.values())

    new_dict[key[0]] = value[0]

    return new_dict


new_dictionary = set_by_path({'a': 1}, ['a', 'b'], 2)
new_dictionary2 = set_by_path({'a': 1}, ['b', 'c', 'd'], 2)
new_dictionary3 = set_by_path({'a': 1}, ['b'], 2)
print(new_dictionary3)
print(new_dictionary)
print(new_dictionary2)

