import math
distance_pc = 33.3
apparent_magnitude = 11.0

absolute_magnitude = (5 - (5*(math.log(distance_pc, 10)))) + 11
print(absolute_magnitude)