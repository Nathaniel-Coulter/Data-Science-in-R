# Importing necessary library
from scipy.stats import binom

# Part 1: Probability that the student leaves her iClicker in the 5th class
def part_1():
    # Probability of leaving the iClicker in the 5th class
    p_leave = 1 / 4
    # The probability that she leaves her iClicker in the 5th class is just p_leave
    probability = p_leave
    return round(probability, 3)  # Return rounded to 3 significant figures

# Part 2: Best chance to retrieve the iClicker if she arrives home without it
def part_2():
    # Since the probability of leaving the iClicker in any class is equal, it doesn't matter which class she tries.
    # So she can try any class, as the probability is the same.
    return "Any class"

# Part 3: Probability she left the iClicker in the 5th class given she arrived home without it
def part_3():
    # Probability of leaving the iClicker in any particular class
    p_leave = 1 / 4
    # Probability she arrived home without the iClicker (i.e., she left it behind in one of the 5 classes)
    p_home_without = 1 / 5
    # Applying Bayes' Theorem
    probability = p_leave / p_home_without
    return round(probability, 3)  # Return rounded to 3 significant figures

# Main function to print results for each part
def main():
    print("Part 1: Probability she leaves her iClicker in the 5th class:", part_1())
    print("Part 2: Best chance of retrieving the iClicker:", part_2())
    print("Part 3: Probability she left the iClicker in the 5th class given she arrived home without it:", part_3())

# Run the program
if __name__ == "__main__":
    main()
