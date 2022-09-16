import numpy as np
from scipy import stats

n = 1000
velocity = stats.weibull_max.rvs(2, loc=107, scale=4, size=n)
angle = stats.norm.rvs(loc=48, scale=7, size=n)
height = 2

throw_angle = np.radians(angle)
throw_velocity = velocity/3.6
throw_velocity_y = throw_velocity * np.cos(throw_angle)
throw_velocity_z = throw_velocity * np.sin(throw_angle)
air_time = (throw_velocity_z + np.sqrt((throw_velocity_z ** 2) + (2 * 9.81 * height)))/9.81
throw_distance = throw_velocity_y * air_time
print(
f'''
Throw distance [R]: {throw_distance}
'''
)

#
values = throw_distance
alpha = 0.05
values.sort()
lower_idx = round(len(values)*(alpha/2))
upper_idx = round(len(values)*(1-(alpha/2))-1)
print(f'lower_index: {lower_idx}')
print(f'upper_index: {upper_idx}')
print(f'lower_value: {values[lower_idx]}')
print(f'upper_value: {values[upper_idx]}')
