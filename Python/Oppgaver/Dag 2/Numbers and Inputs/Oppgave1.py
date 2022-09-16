first_name = input('First name: ')
last_name = input('Last name: ')
course = input('Course: ')
participants = input('Participants: ')

first_name = first_name.lower().capitalize()
last_name = last_name.lower().capitalize()
course = course.lower()

print(f'''My name is {first_name} {last_name}.
I am participation in the course {course}. 
There are {participants} candidates taking the course.''')