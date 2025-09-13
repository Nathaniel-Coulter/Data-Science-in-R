def expected_balls_in_leftmost_container(num_columns, num_balls):
    # The number of rows is one less than the number of columns
    num_rows = num_columns 
   
    # Probability of a ball landing in the leftmost container
    probability_leftmost = (1 / 2) ** num_rows
   
    # Expected number of balls in the leftmost container
    expected_balls = num_balls * probability_leftmost
   
    # Since we can't have a fraction of a ball, we round to the nearest whole number
    return round(expected_balls)

# Example usage
num_columns = 6  # Number of columns in the Quincunx
num_balls = 100  # Number of balls to drop

expected_balls = expected_balls_in_leftmost_container(num_columns, num_balls)
print(f"Expected number of balls in the leftmost container: {expected_balls}")
