def valid_parentheses(string):
    count = 0
    for i in string:
        if i == '(':
            count += 1
        elif i == ')':
            if count == 0:
                return False
            else:
                count -= 1
    return count == 0


string = '(())((()())())'
output = valid_parentheses(string)
print(output)
