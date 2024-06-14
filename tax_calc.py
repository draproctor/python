import sys
from dataclasses import dataclass

import click
from tabulate import tabulate


@dataclass
class TaxBracket:
    rate: float
    minimum: int
    maximum: int
    bonus_tax: int | float = 0

    def tax_owed(self, income: float | int) -> float:
        if income <= self.minimum:
            return 0.0
        income = min(income, self.maximum)
        owed = self.rate * (income - self.minimum - 1) + self.bonus_tax
        print(f"{self.rate} * ({income} - {self.minimum}) = ${owed:,.2f}")
        return owed


@click.command()
@click.argument("taxable_income", type=float)
def main(taxable_income: float) -> None:
    tax_brackets = [
        TaxBracket(rate=0.10, minimum=0, maximum=11_600, bonus_tax=0),
        TaxBracket(rate=0.12, minimum=11_601, maximum=47_150, bonus_tax=0),
        TaxBracket(rate=0.22, minimum=47_151, maximum=100_525, bonus_tax=0),
        TaxBracket(rate=0.24, minimum=100_526, maximum=191_950, bonus_tax=0),
        TaxBracket(rate=0.32, minimum=191_951, maximum=243_725, bonus_tax=0),
        TaxBracket(rate=0.35, minimum=243_726, maximum=609_350, bonus_tax=0),
        TaxBracket(
            rate=0.37, minimum=609_351, maximum=sys.maxsize, bonus_tax=183_647.25
        ),
    ]

    taxes_owed = sum(bracket.tax_owed(taxable_income) for bracket in tax_brackets)

    tax_values = {
        "Income": taxable_income,
        "Tax Owed": taxes_owed,
        "Gross Income": taxable_income - taxes_owed,
        "Pct. Lost to Taxes": "{0:.0%}".format(taxes_owed / taxable_income),
    }
    print(tabulate([tax_values], headers="keys", tablefmt="github"), "\n")

    spendable_monies = {
        "Monthly Gross Income": tax_values["Gross Income"] / 12,
        "Paycheck Value": tax_values["Gross Income"] / 26,
        "Maximum Rent": tax_values["Gross Income"] / 36,
    }
    print(tabulate([spendable_monies], headers="keys", tablefmt="github"))


if __name__ == "__main__":
    main()
