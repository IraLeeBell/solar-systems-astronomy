constant = 2.06e5
wavelength = 5.5e-7
diameter = 6.51
arc_seconds = 0.055

angular_resolution = constant*(wavelength/diameter)
print(angular_resolution)

diameter_2 = constant*(wavelength/arc_seconds)
print(diameter_2)