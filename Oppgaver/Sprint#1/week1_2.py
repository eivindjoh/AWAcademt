# 1. The remainder of 345 after division with 12 (so the remainder after doing 345/12)

print(345 % 12) #svaret er 9

# 2. Create a variable x and set it to 5 and another variable y to 3. Overwrite x to
# have the value x * y. Subtract 5 from x. Now display the result.

x = 5
y = 3
x = x * y
x -= 5
print(x)

# 3. Your friend has 37 oranges and takes 6 for himself. He then splits the remaining
# oranges evenly between 3 of his friends (himself not included and evenly in the sense
# that everyone gets the same amount and an orange cannot be split into parts). How many oranges are left after all 3 friends have gotten their share? Write a python script to calculate this and print the result

oranges_left = (37-6) % 3
print(oranges_left)
