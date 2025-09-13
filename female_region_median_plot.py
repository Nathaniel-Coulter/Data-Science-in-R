
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
file_path = r"C:\Users\hocke\OneDrive\Documents\R Programs (Intro to Data Science Class)\Data Sets\insurance2yrs.csv"
data = pd.read_csv(file_path)

# Parameters
ages = list(range(18, 65))
regions = ["northeast", "northwest", "southeast", "southwest"]
bmi_value = 22
bmi_min = bmi_value * 0.9
bmi_max = bmi_value * 1.1

results = []

def estimate_charge_median(age, sex, region):
    subset = data[
        (data['age'] >= age - 1) & (data['age'] <= age + 1) &
        (data['sex'].str.lower() == sex) &
        (data['region'].str.lower() == region) &
        (data['smoker'].str.lower() == 'no') &
        (data['children'] == 0) &
        (data['bmi'] >= bmi_min) & (data['bmi'] <= bmi_max)
    ]
    if not subset.empty:
        return round(subset['charges'].median(), 2)
    return None

# Loop through age/region combos for females only
for age in ages:
    for region in regions:
        charge = estimate_charge_median(age, 'female', region)
        if charge is not None:
            results.append({
                "age": age,
                "region": region,
                "predicted_charge": charge
            })

# Create and save dataframe
results_df = pd.DataFrame(results)
results_df.to_csv("female_region_median_charges.csv", index=False)

# Plotting
plt.figure(figsize=(12, 6))
for region in regions:
    subset = results_df[results_df['region'] == region]
    plt.plot(subset['age'], subset['predicted_charge'], label=region.title())

overall_avg = round(data['charges'].mean(), 2)
plt.axhline(y=overall_avg, color='gray', linestyle='--', label=f'Overall Avg (${overall_avg})')

plt.title("Estimated Insurance Cost by Region (Healthy Female, Age 18–64, Median)")
plt.xlabel("Age")
plt.ylabel("Predicted Charge ($)")
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.savefig("female_region_charge_median_plot.png")
plt.show()
