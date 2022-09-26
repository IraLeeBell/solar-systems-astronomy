# Find orbital period in minutes of an imaginary satellite orbiting just 1025 km above Earth's surface (Ignore friction with the atmosphere)
import math

'''the gravitational constant is equal to 6.67e-11 m^3/s^2/kg'''
gravitational_constant = 6.67e-11

'''this is the mass of Earth in Kilograms'''
mass_1 = 5.97e24 

'''this is the radius, in meters, of the satellite plus the radius of the Earth from its center to the surface. That numnber is 7405km, but it needs to be converted to meters to match our gravitational constant'''
radius_1 = 7.405e6

period_1 = math.sqrt((((4*(math.pi**2))/(gravitational_constant*mass_1))*radius_1**3))

'''Our answer will be in seconds, so we need to divide it by 60 to convert to minutes'''
print(f'{period_1/60} minutes')

# The moon of a certain planet takes 3.5 days to orbit at a distance of 1.5 x 10^5 km from the center of the planet. What is the total mass (in kg) of the planet-moon system?

'''Convert 3.5 days to seconds, which is 303400'''
period_2 = 302400

'''Convert 1.5e5 km to meters, which is 1.5e8'''
radius_2 = 1.5e8

mass_2 = ((4*(math.pi**2))/(gravitational_constant*(period_2**2)))*(radius_2**3)

print(f'{mass_2} kilograms')
