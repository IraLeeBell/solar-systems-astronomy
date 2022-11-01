# The formula to determine the diameter of a crater is:
# D = 0.003m^(1/4)v^(1/2)
# where D is the crater diameter in kilometers (km), 
# m is the mass of the impactor in kilograms (kg), 
# and v is the velocity in kilometers per second (km/s). 
# This formula is only valid on the Moon. 
# All other terrestrial planetary bodies have a similar formula, 
#but the coefficient varies depending on the composition of the surface.


mass = 1.92e13
velocity = 24

diameter = 0.003*(mass**(1/4))*(velocity**(1/2))
print(diameter)