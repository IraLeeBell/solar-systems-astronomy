import math
# You want to create a telescope with a resolving power of 0.089 arcseconds at a wavelength of 600 nm.
# What diameter (in m) do you need? If you want to increase the light gathering power by a factor of 5, 
# by what factor does the diameter need to increase? What would the new resolving power be for this improved telescope?
plancks_constant = 2.06e5
resolving_power = 0.089
wavelength = 6.00e-7

diameter = plancks_constant*(wavelength/resolving_power)
print(diameter)


# Compare the light-gathering power of a 10 m telescope to that of a 0.5 m telescope
diameter_a = 10
diameter_b = 0.5
light_gathering_power = (diameter_a/diameter_b)**2
print(f'this is light gath: {light_gathering_power}')

# Light gathering Power
diameter = 0.5
area = math.pi * (diameter/2)**2
print(f'this is the light gathering power: {area}')
# 78.53981633974483
# 0.19634954084936207
# Magniying Power
focal_length_primary = 24
focal_length_eyepiece = 2.54
magnifying_power = focal_length_primary/focal_length_eyepiece
print(magnifying_power)

# angular resolution
diameter_5 = 0.2794
wavelenth_5 = 5.5e-7
angular_resultion_5 = plancks_constant*(wavelenth_5/diameter_5)
print(f'This is the angular rez: {angular_resultion_5}')
# 0.02266
# 0.04532