import math

initials = 'EAJ'
pop_hometown = 10725
pop_earth = 7900000000
weekday = 'thursday'
course_duration = 'twelve weeks'
pi = math.pi

my_string = f'''Hi, my initials are {initials} and I come from a small town with a population of
{pop_hometown} people. This is {round(((pop_hometown/pop_earth)*100), 6)}% of the worlds population which is
{pop_earth} people. We are living on a planet that has a surface thats approx. {round(4*pi*6378**2)}
square kilometers. Today its {weekday} and I am preparing for a {course_duration} long course
in data analytics. Did you know that march 14th is the world pi day? Because pi is {round(pi, 2)}.'''

print(my_string)
