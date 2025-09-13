import math

# Define the probability of drawing a heart
p = 13/52

# Define the number of draws
n = 19

# Define the minimum number of hearts required
k = 8

# Calculate the probability of drawing at least k hearts
prob_at_least_k_hearts = 0
for i in range(k, n+1):
    prob_at_least_k_hearts += math.comb(n, i) * (p ** i) * ((1 - p) ** (n - i))

print("The probability of drawing at least 8 hearts is:", prob_at_least_k_hearts)

# Calculate the expected value of X
E_X = n * p
print("The expected value of X is:", E_X)

# Calculate the standard deviation of X
sigma = math.sqrt(n * p * (1 - p))
print("The standard deviation of X is:", sigma)