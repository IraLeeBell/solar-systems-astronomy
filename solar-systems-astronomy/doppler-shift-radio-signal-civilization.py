#km/s
radial_velocity_planet = 30
# cm
true_wavelength_of_radio_signal = 13
# km/s
speed_of_light = 3e5

doppler_shift = true_wavelength_of_radio_signal*(radial_velocity_planet/speed_of_light)
print(doppler_shift)
