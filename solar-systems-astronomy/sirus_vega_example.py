# Sirius is usually 5 times brighter than Vega. If a thin cloud passes in front of Sirius, reducing the flux that reaches Earth by a factor of 4, what is Sirius's new apparent visual magnitude if Vega's is still 0.03?

import math
# Magnitude System - Flux Ratio from Delta M

# MVega - MSirus = 2.5log(FSirus /Fvega)

# We are trying to solve for MSirus. From the question, we know that Sirius is usually 5 times brighter than Vega. Mathematically, this means Fs = 5 Fv

# But now we want to find the new flux of Sirius when there's a cloud reducing its flux by a factor of 4. This means we divide the old flux by 4; mathematically, this translates to: Fs,new = Fs,old / 4

# And since we know that, Fs,old = 5 x Fv, this means that Fs,new = 5 x Fv / 4 = 1.25 x Fv. We can rearrange this equation for the ratio new of fluxes: Fs, new / Fv = 1.25.

# Going back to our original equation, now we know the ratio of the fluxes for the two stars with the cloud between them, and can plug this into the equation: Mvega - MSirus = 2.5log(1.25)

# Plug the right hand side of the equation into a calculator (or google) to find the difference in magnitude between Vega and Sirius with a thin cloud in front of Sirius.

# Now remember we want to solve for MSirus. The other equation we need to use is DeltaM = MVega - MSirus. You just solved the first equation for DeltaM.

# The question tells us that MVega = 0.03. Now, just solve MSirus = MVega - DeltaM = 0.03 - DeltaM to find the new apparent visual magnitude of sirus.


StarNameA = "Sirus"
StarNameB = "Vega"
StarAFlux = 5
StarBFlux = 1
StarAFluxWithCloud = 4
StarBApparentVisualMagnitude = 0.03

StarAMagnitudeWithCloud = 2.5 * math.log10((StarAFlux / StarAFluxWithCloud))

print(f"The difference in magnitude between {StarNameB} and {StarNameB}")
print(f"with a thin cloud in front of {StarNameA} is:") 
print(f"\n\t{StarAMagnitudeWithCloud}")

StarAApparentVisualMagnitude = StarAMagnitudeWithCloud - StarBApparentVisualMagnitude

print(f"The new apparent visual magniutude of {StarNameA} is:")
print(f"\n\t{StarAApparentVisualMagnitude}")