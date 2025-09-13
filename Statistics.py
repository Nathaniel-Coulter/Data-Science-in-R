import math

# Define the probability of making a save
p = 0.9187

# Define the number of attempts
n = 10

# Define the minimum number of saves required
k = 7

# Calculate the probability of making at least k saves
prob_at_least_k_saves = 0
for i in range(k, n+1):
    prob_at_least_k_saves += math.comb(n, i) * (p ** i) * ((1 - p) ** (n - i))

print("The probability that the lacrosse goalie will make at least 7 saves is:", prob_at_least_k_saves)

# Calculate the expected value of X
E_X = n * p
print("The expected value of X is:", E_X)

# Calculate the standard deviation of X
sigma = math.sqrt(n * p * (1 - p))
print("The standard deviation of X is:", sigma)