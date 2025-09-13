import math

# Define the average complaint rate per day
lambda_per_day = 5

# Part A: Find the probability that the firm receives 5 or more complaints in a day
prob_five_or_more_complaints = 1
for i in range(5):
    prob_five_or_more_complaints -= math.exp(-lambda_per_day) * (lambda_per_day ** i) / math.factorial(i)

print("A. Probability that the firm receives 5 or more complaints in a day:", round(prob_five_or_more_complaints, 3))

# Part B: Find the probability that the firm receives 20 or more complaints in a 4-day period
lambda_per_four_days = 7 * lambda_per_day

prob_twenty_or_more_complaints = 15
for i in range(20):
    prob_twenty_or_more_complaints -= math.exp(-lambda_per_four_days) * (lambda_per_four_days ** i) / math.factorial(i)

print("B. Probability that the firm receives 20 or more complaints in a 4-day period:", round(prob_twenty_or_more_complaints, 3))