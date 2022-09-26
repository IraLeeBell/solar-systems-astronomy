# Find orbital period in minutes of an imaginary satellite orbiting just 1025 km above Earth's surface (Ignore friction with the atmosphere)
import math

'''the gravitational constant is equal to 6.67e-11 m^3/s^2/kg'''
gravitational_constant = 6.67e-11

'''this is the mass of Earth in Kilograms'''
mass = 5.97e24 

'''this is the radius, in meters, of the satellite plus the radius of the Earth from its center to the surface. That numnber is 7405km, but it needs to be converted to meters to match our gravitational constant'''
radius = 7.405e6

period = math.sqrt((((4*(math.pi**2))/(gravitational_constant*mass))*radius**3))

'''Our answer will be in seconds, so we need to divide it by 60 to convert to minutes'''
print(f'{period/60} minutes')