#a
students = [
    'Eivind Johansen', 'Randy Cotour',
    'Michael McIntyre', 'Amy Schumer',
    'Michael Schumacher'
    ]

#b
print(students[2])

#c
print(students[2][0])

#d
students[2] = 'Ole'
print(students[2])

#e
students[2] = students[2] + ' Nordmann'
print(students[2])

#f
students.append('Michael McIntyre')
print(students)

#g
students.insert(4, 'Monty Python')
print(students)

#h
print(len(students))
students.remove('Ole Nordmann')
print(len(students))

#i
print(students.index('Monty Python'))

#j
print(students[:3])

#k
print(students[::-1])

#l
students_even = students[::2]
print(students_even)

#m
students_odd = students[1::2]
print(students_odd)


