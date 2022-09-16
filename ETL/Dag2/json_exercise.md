# JSON exercises

## 1 - Remembering the ingredients for your favorite recipes

You love to cook and know many great recipes almost by heart. Unfortunately you often forget the correct amounts of ingredients you need and end up not having enough when you are actually cooking.

0. How would you represent this recipe using a dictionary? What should be the keys and values? Discuss with your classmates.

1. Create a simple script that uses `input()` to gather ingredients and amounts needed in a dictionary.

2. Save the dictionary to a JSON file. Make sure to also ask the user for the recipe's name so you can use that in the filename and collect files in the folder `recipe_archive`.
3. Now write another script that takes an argument (you can accept input to a python script by using `sys.argv`) about the recipe you are trying to remember. The script should then load the matching JSON-file from `recipe_archive` and give a friendly printout on the terminal about which ingredients you will need. Consider a format of

```
For pancakes you will need:
300ml of milk
100g of flour
5 tbsp of sunflower oil
a pinch of salt
```

3. (Bonus) This is actually quite useful so you want to also keep the actual cooking instructions saved along with your ingredients lists. After finishing the ingredients list also ask the user for if they have the cooking instructions ready and accept a filename (e.g. `how_to_cook_risotto.txt`) as input. Read the file and store the content in an additional field of your dictionary under the key `instructions.`
4. You realise that creating so many files is a bit tricky and filenames are not always as nice as the actual names of a dish, so you decide to move everything into a single JSON and create a dict of dicts using the recipe names as the keys and the ingredients dicts as the values.
