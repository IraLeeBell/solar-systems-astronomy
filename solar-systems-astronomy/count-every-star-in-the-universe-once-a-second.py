seconds_in_year = 3.15e7
stars_in_universe = 1.00e22

years_it_takes_to_count = stars_in_universe/seconds_in_year
print(f'It would take {years_it_takes_to_count} years to count the estimated')
print('numbers of stars in the universe if you counted once a second.')
print(f'\nOr, scientific notation if you prefer...' + "{:.2E}".format(float(years_it_takes_to_count)) + ' years.')


