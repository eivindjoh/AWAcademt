'''
2. Create a function that counts the number of “events” in a list and returns a dictionary with the
key value pair {<event>: <numb_of_event>} (an “event” is just the occurrence of a certain value,
feel free to just try it out with numbers or words)
Possible inputs could be
• [“heads”, “heads”, “tails”, “heads”]
• [6, 6, 6, 7, 7, 7, 8, 8, 11, 11, 11, 11, 12]
'''


def count_of_events(input_list):
    unique_values = set(input_list)
    dick = {}
    for i in unique_values:
        dick[i] = input_list.count(i)
    return dick


output = count_of_events([1, 2, 3, 4, 5, 5, 5, 3, 3, 3])
output2 = count_of_events(['heads', 'heads', 'tails', 'tails', 'heads', 'heads'])

print(output)
print(output2)
