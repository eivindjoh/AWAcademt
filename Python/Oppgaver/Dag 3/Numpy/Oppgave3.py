import numpy as np

angles = np.array([35, 45, 45, 50, 55])
velocities = np.array([35, 40, 45, 50, 55])
heights = np.array([0, 1, 2, 3, 4])

throw_angle = np.radians(angles)
throw_velocity = velocities/3.6
throw_velocity_y = throw_velocity * np.cos(throw_angle)
throw_velocity_z = throw_velocity * np.sin(throw_angle)
air_time = (throw_velocity_z + np.sqrt((throw_velocity_z ** 2) + (2 * 9.81 * heights)))/9.81
throw_distance = throw_velocity_y * air_time
print(
f'''
Throw angle in radians [alpha]: {throw_angle}
Throw velocity in m/s [v_0]: {throw_velocity}
Throw velocity in the horizontal direction [v_x]: {throw_velocity_y}
Throw velocity in the vertical direction [v_y]: {throw_velocity_z} 
Airtime [t]: {air_time}
Throw distance [R]: {throw_distance}
'''
)


