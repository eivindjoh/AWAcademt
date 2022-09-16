thedictionary = {"A": 2, "B": {"F": [1,2,3]}, 5: [5,6,7], 10: True, "D": "100 10"}

value = thedictionary["D"].split(" ")
value = "".join(value)
print(value)
