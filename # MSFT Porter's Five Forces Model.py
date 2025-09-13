# MSFT Porter's Five Forces Model 

import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

forces = [
"Competitive Rivalry",
"Bargaining Power of Buyers",
"Bargaining Power of Suppliers",
"Threat of Substitutes",
"Threat of New Entrants"
]
intensity = [5, 3, 2, 2.5, 1] 

plt.figure(figsize=(8, 5))
plt.barh(forces, intensity, color=["red", "orange", "yellow", "lightblue", "green"])
plt.xlabel("Intensity (1 = Low, 5 = High)")
plt.title("Microsoft - Porter's Five Forces Analysis (2024)")
plt.gca().invert_yaxis()

plt.show()
