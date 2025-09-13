

import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
file_path = r"C:\\Users\\hocke\\OneDrive\\Documents\\R Programs (Intro to Data Science Class)\\Data Sets\\insurance2yrs.csv"
data = pd.read_csv(file_path)

# Parameters
ages = list(range(18, 65))
regions = ["northeast", "northwest", "southeast", "southwest"]
bmi_value = 22
bmi_min = bmi_value * 0.9
bmi_max = bmi_value * 1.1
min_matches = 4  # Exclude estimates based on fewer than this many individuals

results = []

def estimate_charge(age, sex, region):
    subset = data[
        (data['age'] >= age - 1) & (data['age'] <= age + 1) &
        (data['sex'].str.lower() == sex) &
        (data['region'].str.lower() == region) &
        (data['smoker'].str.lower() == 'no') &
        (data['children'] == 0) &
        (data['bmi'] >= bmi_min) & (data['bmi'] <= bmi_max)
    ]
    if len(subset) >= min_matches:
        return round(subset['charges'].mean(), 2)
    return None

# Main loop: average male and female estimates if both valid
for age in ages:
    for region in regions:
        charges = []
        for sex in ['male', 'female']:
            charge = estimate_charge(age, sex, region)
            if charge is not None:
                charges.append(charge)
        if charges:
            avg_charge = round(sum(charges) / len(charges), 2)
            results.append({
                "age": age,
                "region": region,
                "predicted_charge": avg_charge
            })

# Create DataFrame and save
results_df = pd.DataFrame(results)
results_df.to_csv("region_charge_simulation_combined_filtered.csv", index=False)

# Plotting
plt.figure(figsize=(12, 6))
for region in regions:
    subset = results_df[results_df['region'] == region]
    plt.plot(subset['age'], subset['predicted_charge'], label=region.title())

overall_avg = round(data['charges'].mean(), 2)
plt.axhline(y=overall_avg, color='gray', linestyle='--', label=f'Overall Avg (${overall_avg})')

plt.title("Estimated Insurance Cost by Region (Filtered Healthy Adults, Age 18–64)")
plt.xlabel("Age")
plt.ylabel("Predicted Charge ($)")
plt.legend()
plt.grid(True)
plt.tight_layout()

# Save plot
plt.savefig("combined_region_charge_filtered_plot.png")
plt.show()
