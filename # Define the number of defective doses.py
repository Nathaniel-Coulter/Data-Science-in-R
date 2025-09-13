import math

# Define the mean accidents per week
lambda_per_week = 4

# Define the mean accidents per day
lambda_per_day = lambda_per_week / 7

# A. No accidents occur in one week
prob_no_accidents_week = math.exp(-lambda_per_week)
print("A. Probability of no accidents in one week:", prob_no_accidents_week)

# B. 10 or more accidents occur in a week
prob_at_least_10_accidents_week = 1
for i in range(10):
    prob_at_least_10_accidents_week -= math.exp(-lambda_per_week) * (lambda_per_week ** i) / math.factorial(i)
print("B. Probability of 10 or more accidents in a week:", prob_at_least_10_accidents_week)

# C. One accident occurs today
prob_one_accident_today = math.exp(-lambda_per_day) * (lambda_per_day ** 1) / math.factorial(1)
print("C. Probability of one accident today:", prob_one_accident_today)