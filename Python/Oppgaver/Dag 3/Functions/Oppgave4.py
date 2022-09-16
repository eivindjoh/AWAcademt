import math

def kmh_to_ms(velocity: float) -> float:
    """
    Converts kmh to ms

    :param velocity: float
    :return: float
    """
    return velocity/3.6


def velocity_decomposition(velocity: float, angle: float) -> tuple:
    """
    Calculates throw velocity x and y. Returns tuple

    :param velocity: float
    :param angle: float
    :return: tuple
    """
    throw_velocity_x = velocity * math.cos(angle)
    throw_velocity_y = velocity * math.sin(angle)
    return throw_velocity_x, throw_velocity_y


def airtime(velocity_y, init_height, g=9.81):
    value = (velocity_y + math.sqrt((velocity_y ** 2) + (2 * g * init_height))) / g
    return value

def throw_distance(angle, velocity, init_height=1.8):
    throw_angle = math.radians(angle)
    throw_velocity = kmh_to_ms(velocity)
    throw_velocity_x = velocity_decomposition(throw_velocity, angle)[0]
    throw_velocity_y = velocity_decomposition(throw_velocity, angle)[1]
    air_time = airtime(throw_velocity_y, init_height)
    throw_distance = throw_velocity_y * air_time
    print(
    f'''
    Throw angle in radians [alpha]: {round(throw_angle, 2)}
    Throw velocity in m/s [v_0]: {round(throw_velocity, 2)}
    Throw velocity in the horizontal direction [v_x]: {round(throw_velocity_x, 2)}
    Throw velocity in the vertical direction [v_y]: {round(throw_velocity_y, 2)} 
    Airtime [t]: {round(air_time, 2)}
    Throw distance [R]: {round(throw_distance, 2)}
    '''
    )


angle = float(input('Vinkel (grader): '))
velocity = float(input('Hastighet (km/t): '))
height = float(input('Høyde (m): '))
throw_distance(angle, velocity, height)


