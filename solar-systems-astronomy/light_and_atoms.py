# Cosmic Matter - Light and Atoms 
# by: Ira Bell       Version 0.1 
# Copyright (c) 2022 Space Elements
#
# Calculate the difference in energy (eV) when a photon
# is absorbed (excitation) or emitted (deexcitation)

import os
import time
import math

# Energy levels for a hydrogen atom
level_1 = -13.6
level_2 = -3.40
level_3 = -1.51
level_4 = -0.850
level_5 = -0.544
level_6 = -0.378

# Formula used:
# Ey = Ef - Ei
# Whereby, Ey = Radiation of single photon/light particle
# Ef = Final State
# Ei = Initial State
ei_value = 0
ef_value = 0
def radiation(initial_state, final_state):
	if int(initial_state) == 1:
		ei_value = level_1
	elif int(initial_state) == 2:
		ei_value = level_2
	elif int(initial_state) == 3:
		ei_value = level_3
	elif int(initial_state) == 4:
		ei_value = level_4
	elif int(initial_state) == 5:
		ei_value = level_5
	else:
		ei_value = level_6

	if int(final_state) == 1:
		ef_value = level_1
	elif int(final_state) == 2:
		ef_value = level_2
	elif int(final_state) == 3:
		ef_value = level_3
	elif int(final_state) == 4:
		ef_value = level_4
	elif int(final_state) == 5:
		ef_value = level_5
	else:
		ef_value = level_6	
	ey_value = ef_value-ei_value
	abs_ey_value = abs(ey_value)
	frequency = abs_ey_value / 4.136e-15
	print('\n\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
	print(f'\n* With an initial state of level {initial_state} the Ei value is: {ei_value}')
	print(f'* With a final state of level {final_state} the Ef value is: {ef_value}')
	print(f'\nApplying the data to the formula Ey = Ef ({ef_value}) - Ei ({ei_value})...')
	print(f'\n\n\tThis results in an Ey value of: {ey_value}')
	print(f'\t...with an absolute value of {abs_ey_value}')
	print(f'\n\nTo calculate the frequency using E ({abs_ey_value}) = h (4.136e-15)* f:')
	print(f'\n\tThis results in a frequency of {frequency} or ' + "{:.2E}".format(float(frequency)))
	print(f'\n\t...which is in the ' + frequency_type(float(frequency)) + ' electromagnetic spectral region.')
	print(f'\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
	return

def frequency_type(frequency):
	examine_frequency = float(frequency)
	if examine_frequency < 3e9:
		return "Radio"
	elif examine_frequency >= 3e9 and examine_frequency < 3e12:
		return "Microwave"
	elif examine_frequency >= 3e12 and examine_frequency < 4.3e14:
		return "Infrared"
	elif examine_frequency >= 4.3e14 and examine_frequency < 7.5e14:
		return "Visible"
	elif examine_frequency >= 7.5e14 and examine_frequency < 3e16:
		return "Ultraviolet"
	elif examine_frequency >= 3e16 and examine_frequency < 3e19:
		return "X-rays"
	else:
		return "Gamma Rays"
# Breaking out copyright/credit and allow for sub-routine
def main_program():
	print("-=-=   Cosmic Matter - Light and Atoms     =-=-")
	print("-=-=   by: Ira Bell       Version 0.1     =-=-")
	print("-=-=   Copyright (c) 2022 Space Elements  =-=-")
	sub_program()

# Main sub-routine
def sub_program():
	
	while True:
		print(f"\nPlease enter the level of the initial state:\n\n[Options]:\n\n[1, 2, 3, 4, 5, 6], 'cls' to clear screen or 'q' to quit.")
		initial_state = input("\n>>> ")
		# Check for string input, and whether user wants to quit or clear the screen... or isn't complying w/ the options presented
		if isinstance(initial_state, str):
			if initial_state == 'q' or initial_state == 'Q' or initial_state == 'quit' or initial_state == 'QUIT':
				print('\nExiting program....')
				quit()
			elif initial_state == 'cls':
				clear = lambda: os.system('cls')
				clear()
				main_program()
			print(f'\nThe input for the initial state was not understood, please try again.')
			initial_state = 1
			sub_program()
		elif int(initial_state) >= 1 and int(initial_state) < 7:
			print(f'\nThe input for the initial state of {initial_state} is acceptable.')
		else:
			print(f'\nThe input for the initial state was not understood, restarting program.')
			initial_state = 1
			sub_program()
		print(f"\nPlease enter the level of the final state:\n\n[Options]:\n\n[1, 2, 3, 4, 5, 6], 'cls' to clear screen or 'q' to quit.")
		final_state = input("\n>>> ")
		# Check if user wants to quit
		if isinstance(final_state, str):
			if final_state == 'q' or final_state == 'Q' or final_state == 'quit' or final_state == 'QUIT':
				print('\nExiting program....')
				quit()
			elif initial_state == 'cls':
				clear = lambda: os.system('cls')
				clear()
				main_program()
			print(f'\nThe input for the final state was not understood, please try again.')
			initial_state = 1
			sub_program()
		elif int(final_state) >= 1 and int(final_state) < 7:
			print(f'\nThe input for the final state of {final_state} is acceptable.')
		else:
			print(f'\nThe input for the final state was not understood, restarting program.')
			final_state = 1
			sub_program()
		radiation(initial_state, final_state)
		time.sleep(5)
		print('\n...')
		print('....')
		print('Back to main menu...\n')
		sub_program()
	sub_program()

# Run main program 
main_program()

