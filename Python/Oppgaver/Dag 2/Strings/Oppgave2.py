first_name = 'eiVind'
last_name = 'joHansen'
course = 'dAta enGineEring and analytics'
participants = '9'

first_name = first_name.lower().capitalize()
last_name = last_name.lower().capitalize()
course = course.lower()

print(f'''My name is {first_name} {last_name}.
I am participation in the course {course}. 
There are {participants} candidates taking the course.''')