import math

def my_sum(x, y):
    return x + y

def my_subtract(x, y):
    return x - y

def my_multiply(x, y):
    return x * y

def my_divide(x, y):
    return x / y

def my_throw(angle, velocity, height):
    throw_angle = math.radians(angle)
    throw_velocity = velocity/3.6
    throw_velocity_y = throw_velocity * math.cos(throw_angle)
    throw_velocity_z = throw_velocity * math.sin(throw_angle)
    air_time = (throw_velocity_z + math.sqrt((throw_velocity_z ** 2) + (2 * 9.81 * height)))/9.81
    throw_distance = throw_velocity_y * air_time
    print(
    f'''
    Throw angle in radians [alpha]: {round(throw_angle, 2)}
    Throw velocity in m/s [v_0]: {round(throw_velocity, 2)}
    Throw velocity in the horizontal direction [v_x]: {round(throw_velocity_y, 2)}
    Throw velocity in the vertical direction [v_y]: {round(throw_velocity_z, 2)} 
    Airtime [t]: {round(air_time, 2)}
    Throw distance [R]: {round(throw_distance, 2)}
    '''
    )

action = int(input(
'''Velg kalkulator:
1 = Addere
2 = Subtrahere
3 = Multiplisere
4 = Dividere
5 = Kaste en ball
>>: '''
))

if action == 5:
    angle = float(input('Vinkel (grader): '))
    velocity = float(input('Hastighet (km/t): '))
    height = float(input('Høyde (m): '))
    my_throw(angle, velocity, height)
else:
    x = float(input('X =: '))
    y = float(input('Y =: '))

    if action == 1:
        print(my_sum(x, y))
    elif action == 2:
        print(my_subtract(x, y))
    elif action == 3:
        print(my_multiply(x, y))
    elif action == 4:
        print(my_divide(x, y))





