#!/usr/bin/env python3

import sys
from tabulate import tabulate


try:
    taxable_income = int(sys.argv[1])
except ValueError:
    print(f"{sys.argv[1]} is not a valid number for calculating a taxable income.")
    exit(1)

# single filer brackets from https://www.nerdwallet.com/article/taxes/federal-income-tax-brackets
bracket_limits = {
    (518_401, sys.maxsize): lambda x: 156235 + (0.37 * (x - 518400)),
    (207_351, 518_400): lambda x: 47367.5 + (0.35 * (x - 207350)),
    (163_301, 207_350): lambda x: 33271.5 + (0.32 * (x - 163300)),
    (85_526, 163_300): lambda x: 14605.5 + (0.24 * (x - 85525)),
    (40_126, 85_525): lambda x: 4617.5 + (0.22 * (x - 40125)),
    (9876, 40_125): lambda x: 987.5 + (0.12 * (x - 9875)),
    (0, 9875): lambda x: 0.10 * x,
}

selected_bracket = None

for income_bounds, tax_bracket_calc in bracket_limits.items():
    lower_bound = income_bounds[0]
    upper_bound = income_bounds[1]
    if lower_bound < taxable_income and taxable_income < upper_bound:
        selected_bracket = tax_bracket_calc
        break

if selected_bracket == None:
    print(f"No tax bracket satisfied the range. What the hell is {taxable_income}?")
    exit(1)

tax_owed = selected_bracket(taxable_income)
gross_yearly_income = taxable_income - tax_owed

tax_values = {
    "Income": taxable_income,
    "Tax Owed": selected_bracket(taxable_income),
    "Gross Income": gross_yearly_income,
    "Pct. Lost to Taxes": "{0:.0%}".format(tax_owed / taxable_income),
}
print(tabulate([tax_values], headers="keys", tablefmt="github"), "\n")

spendable_monies = {
    "Monthly Gross Income": gross_yearly_income / 12,
    "Paycheck Value": gross_yearly_income / 26,
    "Maximum Rent": gross_yearly_income / 36,
}
print(tabulate([spendable_monies], headers="keys", tablefmt="github"))
