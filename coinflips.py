#%% imports

import pandas
import math
from matplotlib import pyplot

#%% calculate in how many ways we can get n (repeats) heads across certain flips of a coin
def combination(flips, repeats):
    return math.factorial(flips)/(math.factorial(repeats) * math.factorial(flips - repeats))

#%% define variables
flips = 5
outcomes = 2**flips

outcomeCounts = []

#calculate propability quick way: (propability of a single outcome) ** coin flips 
probv1 = (1/2) ** flips

#calculate propability long way: number of ways to get n heads/total number of possible outcomes
probv2 = combination(flips, 5)/outcomes

print(f"Option 1. Probability of {flips} heads in a row: {probv1}")
print(f"Option 2. Probability of {flips} heads in a row: {probv2}")

# %%

#%% visualize number possible outcomes of n heads

#calculate all ways to get all numbers of heads (for chart)
i = 0
while i <= flips:
    outcomeCounts.insert(0, [i, combination(flips, i)])
    i += 1

dt = pandas.DataFrame(data = outcomeCounts, columns = ["Result", "Number of repeats"])

figureOne = pyplot.figure()
series = figureOne.add_axes([0,0,1,1])

series.bar(dt["Result"], dt["Number of repeats"])

series.set_ylabel("Number of ways to get")
series.set_xlabel("Number of heads")
series.set_title(str(flips) + " flips")

pyplot.show()
