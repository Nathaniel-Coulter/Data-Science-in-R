# Dr. Mason Asset Allocation

import matplotlib.pyplot as plt

asset_classes = [
    "Fixed Income (Bonds, TIPS, Municipal Bonds)",
    "Equities (Large-Cap, Dividend Stocks, REITs)",
    "Alternative Investments (Private Equity, Infrastructure, Royalty Income Fund)",
    "Cash & Short-Term Investments"
]

target_allocations = [50, 30, 10, 10]

purposes = [
    "Provides stability and income, hedging against inflation.",
    "Growth-oriented with steady income from dividends.",
    "Diversification and potential alignment with their intellectual property.",
    "Provides liquidity for immediate needs and emergencies."
]

fig, ax = plt.subplots()
ax.pie(target_allocations, labels=asset_classes, autopct='%1.1f%%', startangle=90)
ax.axis('equal')  

description = "\n".join([f"{asset_classes[i]}: {purposes[i]}" for i in range(len(asset_classes))])
plt.gca().text(0, -1.5, description, fontsize=10, ha='center', va='top', bbox=dict(facecolor='white', alpha=0.5))

plt.title('Asset Allocation Strategy')

plt.show()