dic1 = {
    1: 10,
    2: 20
    }
dic2 = {
    3: 30,
    4: 40
    }
dic3 = {
    5: 50,
    6: 60
    }

new_dictionary = {**dic1, **dic2, **dic3}
print(new_dictionary)


'''def unfold_dict(dictionary):
    n_dictionary = {}
    for key, value in dictionary.items():'''


input_dict = {
    'a': {'d': 1, 'e': 2},
    'b': {'f': 3},
    'c': {'g': 4, 'h': 5}
    }


def unfold_dict(**kwargs):
    n_dict = {}
    for count_x, (key, value) in enumerate(kwargs.items()):
        s = list(kwargs.keys())
        v_keys = list(kwargs.get(key).keys())
        v_values = list(kwargs.get(key).values())
        for count_y, i in enumerate(v_keys):
            n_dict[s[count_x]+v_keys[count_y]] = v_values[count_y]
    return n_dict


def new_unfold_dict(**kwargs):
    n_dict = {}
    for key, value in kwargs.items():
        for sub_key, sub_value in value.items():
            new_key = key + sub_key
            n_dict[new_key] = sub_value
    return n_dict

unpacked_dict = unfold_dict(**input_dict)
print(unpacked_dict)
new_unpacked_dict = (new_unfold_dict(**input_dict))
print(new_unpacked_dict)
