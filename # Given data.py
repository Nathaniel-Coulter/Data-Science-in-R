EBIT = 300  
tax_rate = 0.35  
depreciation = 20  
capital_expenditures = 60  
increase_in_NWC = 30  

NOPAT = EBIT * (1 - tax_rate)

FCFF = NOPAT + depreciation - capital_expenditures - increase_in_NWC


print(f"Free cash flow to the firm = {FCFF}")
