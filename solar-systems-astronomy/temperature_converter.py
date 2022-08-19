import os
# The following program converts any F -> K, F -> C, K -> F, K -> C,
# C -> F, and C -> K

# C = Celsius
# F = Fahrenheit
# K = Kelvin

# fahrenheit to kelvin
# (32°F − 32) × 5/9 + 273.15 = 273.15K

# celsius to kelvin
# kelvin = celsius + 273.15

# c to f
# fahrenheit = (celsius x 1.8) + 32

def celsius_input(celsius):
	fahrenheit = (celsius x 1.8) + 32
	kelvin = celsius + 273.15

while True:
	print(f"\nPlease input the temperature classification you would like to convert from [c, f, k] or 'q' to quit.")
	
	temperature_classification = input("\n>>> ")
	
	if temperature_classification == 'q' or temperature_classification == 'Q':
		break
	if temperature_classification == 'c' or temperature_classification == 'C':
		print("You have selected Celsius.")
		celsius = input("Please enter the temperature in celsius.\n>>>")
		print("...calculating...")
		print(f"\n{celsius} Celsius converts to:")
		print(f"\t{celsius_input(celsius)} ")
	elif temperature_classification == 'f' or temperature_classification == 'F':
		print("You have selected Fahrenheit.")
	elif temperature_classification == 'k' or temperature_classification == 'K':
		print("You have selected Kelvin.")
	else:
		clear = lambda: os.system('cls')
		clear()

