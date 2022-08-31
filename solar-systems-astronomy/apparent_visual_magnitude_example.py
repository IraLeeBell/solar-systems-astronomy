#  Star A has an apparent visual magnitude of 7 and 3 times as much light per unit area per unit time reaches Earth compared to Star B. What is the apparent visual magnitude of Star B?

# For this question, you are going to use the magnitude - flux relation: Mb - Ma - 2.5log(Fa/Fb)


# We are solving for Mb. The question tells us that 3 times as much light per unit area per unit time reaches Earth from Star A as it does from Star B. Remember that light per unit time per unit area is the same thing as flux, so that means Fa = 3Fb, so Fa/Fb = 3


# Additionally, the question tells us that Ma = 7. Now we can solve the original equation for the magnitude of Star B. We end up with Mb = 2.5log(Fa/Db) + Ma = 2.5log(3) + 7


# So just solve that last part of the equation using a calculator or Google and you'll end up with the apparent visual magnitude of star B.
import math

StarA = "Star A"
StarB = "Star B"
StarAFlux = 3
StarBFlux = 1
StarAApparentVisualMagnitude = 7

StarBApparentVisualMagnitude = (2.5 * math.log10((StarAFlux / StarBFlux))) + StarAApparentVisualMagnitude

print(f"The apparent visual magnitude of {StarB} is:")
print(f"\n\t{StarBApparentVisualMagnitude}")
