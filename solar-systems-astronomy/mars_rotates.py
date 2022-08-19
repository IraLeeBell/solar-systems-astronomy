# Imagine if mars took 205,000 minutes to go around the sun.
# Is this plausible?

mars_minutes = 205_000
mars_hours = mars_minutes / 60
mars_days = mars_hours / 24
mars_years = mars_days / 365
mars_years_formatted = "{:.3f}".format(mars_years)

print(f"This would mean that Mars rotates around the sun in:")
print(f"\tDays: {mars_days}")
print(f"\tYears: {mars_years_formatted}")