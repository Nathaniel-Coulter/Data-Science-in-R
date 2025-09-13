# Part A: Calculate the standard deviation of the number of hours cars are parked
hours = [1, 2, 3, 4, 5, 6, 7, 8]
probabilities = [0.233, 0.106, 0.127, 0.089, 0.066, 0.039, 0.034, 0.306]

mean_hours = sum([hour * prob for hour, prob in zip(hours, probabilities)])
variance_hours = sum([(hour - mean_hours) ** 2 * prob for hour, prob in zip(hours, probabilities)])
std_dev_hours = variance_hours ** 0.5

print("A. Standard Deviation of the number of hours cars are parked:", round(std_dev_hours, 3))

# Part B: Calculate the standard deviation of the amount of revenue each car generates
revenues = [hour * 4.75 for hour in hours]
mean_revenue = sum([revenue * prob for revenue, prob in zip(revenues, probabilities)])
variance_revenue = sum([(revenue - mean_revenue) ** 2 * prob for revenue, prob in zip(revenues, probabilities)])
std_dev_revenue = variance_revenue ** 0.5

print("B. Standard Deviation of the amount of revenue each car generates:", round(std_dev_revenue, 3))