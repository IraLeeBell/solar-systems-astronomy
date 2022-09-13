# calculate the angular diameter using the width of an object and the distance to the object

input_d_width_of_object = 2500
input_D_distance_to_object = 123
input_a_angular_diameter = 1620
output_a_angular_diameter = (input_d_width_of_object * 2.06E5) / input_D_distance_to_object



# An object appears to be 0.45 degrees wide in the sky. If the object's diameter is 2500 km, how far away is it (in km?)
#
# First we want to convert our angular measurement from degrees to arcseconds. 1 degree = 60 arcminutes, and 1 arcminute = 60 arcseconds. So 1 degree = 60 * 60 = 3600 arcseconds. Our angular measurement is 0.45 degrees, so we multiply it by 3600 arcseconds (per 1 degree) to get 0.45 * 3600 = 1620 arcseconds.
#
# So we know the angular diameter and the diameter of the object, now we want to solve for the distance to the object. We'll use the angular diameter version of the small angle formula, rearranged to solve for Dkm. Then plug in d and a to solve for the distance. 
#
# Dkm = (dkm * 2.06e5) / a


D_distance = (input_d_width_of_object * 2.06e5) / input_a_angular_diameter
print(D_distance)

# 1 arc second is 1/3600 of 1 degree




 # Small Angle Formula, better explained
 #
 #
 # (angular diameter in arc seconds)      linear diameter
 # _________________________________   =  ---------------
 #            2.06e5                         distance
 #
 #
 # linear diameter and distance need to be in the same units

 
