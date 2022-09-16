
## Exercises JSON 

Given the file users.json
1. Load the file to a dict in Python
2. Create a function all_names(user_dict) that accepts a dict as input and returns all names as a list
   I.e it should return ["Mysil Bergsprekken", "Reodor Felgen", "Rudolf Blodstrupmoen"]
3. Create a function find_hobbies(user_dict, hobby). It should return the name of all users that has the given hobby.
   I.e find_hobbies(user_dict, "Cars") should return ["Mysil Bergsprekken", "Reodor Felgen", "Rudolf Blodstrupmoen"], while find_hobbies(user_dict, "Grand Prix") should return ["Reodor Felgen"] 
5. Create a new function create_hobby_dict(user_dict) that returns a dictionary that lists each name of each hobby with hobby as the key.
   create_hobby_dict(user_dict) should return
   {
    "Cars" : ["Mysil Bergsprekken", "Reodor Felgen", "Rudolf Blodstrupmoen"],
    "Grand Prix" : ["Reodor Felgen"],
    "Sabotaging" : ["Rudolf Blodstrupmoen"],
   }
6. Write the new dict you just created to a new json file `hobbies.json`.