#a
var_1, var_2, var_3 = 1, 2, 3

#b
temp_var_1, temp_var_2 = var_1, var_2
var_1, var_2 = temp_var_2, temp_var_1
print(var_1, var_2, var_3)

#c
var_1, var_2 = var_2, var_1
print(var_1, var_2, var_3)
