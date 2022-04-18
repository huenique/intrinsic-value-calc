# intrinsic value calculator

Tools based on popular formulas for calculating the intrinsic value of a stock.

Usage example:
```python
from intrinsic_value_calc.financial_ratio import iv_by_pe_ratio
from intrinsic_value_calc.formulas import eps_growth_rate

# Data from https://edge.pse.com.ph/openDiscViewer.do?edge_no=a878e6cd6b389d273470cea4b051ca8f
eps = 173.18  # Earnings/(Loss) Per Share (Basic)
r = eps_growth_rate(173.18, 135.04, 2) / 100
pe_ratio = 15.022  # Price/Earnings Ratio
intrinsic_value = iv_by_pe_ratio(eps, r, pe_ratio)
print(intrinsic_value)
```
