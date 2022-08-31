import math
# Magnitude System - Flux Ratio from Delta M

StarNameA = "Sirus"
StarNameB = "Polaris"
StarAFlux = 24.2
StarBFlux = 1

Magnitude = 2.5 * (math.log10(StarAFlux / StarBFlux))


print(Magnitude)
print(f"This means that the flux from star A is")