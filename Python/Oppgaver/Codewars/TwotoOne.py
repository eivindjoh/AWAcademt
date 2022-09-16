def longest(a1, a2):
    string = a1 + a2
    a = ''
    for i in string:
        if i not in a:
            a += i
    a = ''.join(sorted(a))
    return a



print(longest("loopingisfunbutdangerous", "lessdangerousthancoding"))

d = "loopingisfunbutdangerous"
e = "lessdangerousthancoding"
sett = set(d + e)
print(''.join(sorted(sett)))
