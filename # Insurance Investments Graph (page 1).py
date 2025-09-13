# Insurance Investments Graph (page 1)

import matplotlib.pyplot as plt

# Sample data: General vs Separate Account investment allocations (based on provided notes)
labels = ['Bonds', 'Stocks', 'Mortgages & Real Estate', 'Policy Loans', 'Misc Assets']
general_account = [71, 2, 10, 4, 13]
separate_account = [13, 82, 0.8, 0, 5]

x = range(len(labels))

plt.figure(figsize=(10, 5))
bar_width = 0.35

plt.bar(x, general_account, width=bar_width, label='General Account', color='skyblue')
plt.bar([i + bar_width for i in x], separate_account, width=bar_width, label='Separate Account', color='lightgreen')

plt.xlabel('Asset Class')
plt.ylabel('Percentage Allocation')
plt.title('Insurance Investment Allocations by Account Type')
plt.xticks([i + bar_width / 2 for i in x], labels, rotation=45)
plt.legend()
plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.savefig('/mnt/data/insurance_investment_allocation_chart.png')
plt.show()