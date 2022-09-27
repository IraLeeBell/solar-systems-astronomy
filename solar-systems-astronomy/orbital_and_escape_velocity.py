import math
# circular velocity

'''the gravitational constant is equal to 6.67e-11 m^3/s^2/kg'''
gravitational_constant = 6.67e-11

'''mass of object being orbited'''

earth_mass = 2.00e17
earth_moon_distance = 436000000

circular_velocity = math.sqrt((gravitational_constant*earth_mass)/earth_moon_distance)
print(f'{circular_velocity} m/s')


# escape velocity

radius_earth = 26000

escape_velocity = math.sqrt((2 * gravitational_constant * earth_mass)/radius_earth)
print(f'{escape_velocity} m/s')




r = (2*gravitational_constant*earth_mass)/(3640.2772381818195**2)
print(r)
