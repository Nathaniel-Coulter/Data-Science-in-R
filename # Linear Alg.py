import numpy as np

# Define the augmented matrix
A = np.array([[1, 2, -3, 3],
              [0, 1, 4, -2],
              [0, 0, 0, 0]])  # No inconsistency in last row

# Check for inconsistency (last row should not be [0, 0, 0, c] with c ≠ 0)
if np.any((A[:, :-1] == 0).all(axis=1) & (A[:, -1] != 0)):
    print("There is no solution.")  # This correctly checks for inconsistency
else:
    # System is consistent, solve for general solution
    t = "t"  # Let x3 be the free variable

    # Solve for x1 and x2 in terms of x3
    x3 = t  # Free variable
    x2 = f"-2 - 4{t}"
    x1 = f"7 + 11{t}"

    print(f"x1 = {x1}, x2 = {x2}, x3 is free")