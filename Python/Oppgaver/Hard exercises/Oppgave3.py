'''
3.  Imagine a table setup for our classroom (feel free to draw with a pen first):
a. Create a function that takes everyone in the academy-class as input, and returns a
random seating based on the layout of the class.
b. Upgrade the function to a class, and make sure next time you call it the same people in
the class will not sit next to each other. So no one should sit next to each other two
times in a row.
c. Add a method called visualize() and make a nice print in console of the seating.
(|><-_= are your friends)
'''
import random
class Shuffle:
    students = None

    def __init__(self, students):
        Shuffle.students = students


'''def shuffle_students():
    
    seated = {}
    for i in range(len(students)):
        student = random.choice(students)
        students.remove(student)
        seated[f'seat {i + 1}'] = student
    return seated'''


students = ['Pontus', 'Erlend', 'John', 'Lars', 'Jan Vidar', 'Eivind', 'Serhat', 'Magnus', 'Daniel']
output = Shuffle(students)
output2 = Shuffle(students)
print(Shuffle.students)
print(output.students)
'''print(output)'''




