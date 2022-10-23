# Planet Radius (compared to Earth)
# Re = (drop%/100%)^(1/2) * Star Radius * 109

# Planet Radius (compared to Jupiter)
#Rj = Re * 0.0892

# Kepler's 3rd Law
# period ^ 2 * star mass = orbital radius ^ 3

luminosity = 2.184
temperature = 6465
mass = 1.25
radius = 1.19
period_days = 290
period_years = 0.7945205479452054

orbital_radius = ((period_years**2) * mass)**(1/3)
print(orbital_radius)

radius_earth = ((0.14000000000000057/100)**(1/2))*radius*109
print(radius_earth)

radius_jupiter = radius_earth * 0.0892
print(radius_jupiter)

