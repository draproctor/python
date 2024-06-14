#!/usr/bin/env python3

import sys
from dataclasses import dataclass
import matplotlib.pyplot as plt


@dataclass
class SalesRange:
    minimum: int
    maximum: int

    def __contains__(self, sales: float | int) -> bool:
        return self.minimum <= sales


@dataclass
class CommissionBracket:
    rate: float
    sales_range: SalesRange

    def sales_bonus(self, sales: float | int) -> float:
        if sales < 0:
            raise ValueError("How did you lose money in a sale?")
        if sales not in self.sales_range:
            return 0.0
        # A bracket only applies to the maximum amount of sales in its range.
        sales = min(sales, self.sales_range.maximum)
        bonus = self.rate * (sales - self.sales_range.minimum)
        print(f"{self.rate} * ({sales} - {self.sales_range.minimum}) = ${bonus:,.2f}")
        return bonus


def get_bonus_from_total_sales(total_sales: int) -> float:
    ranges = {
        0.28: SalesRange(600_000, sys.maxsize),
        0.21: SalesRange(525_000, 600_000 - 1),
        0.19: SalesRange(400_000, 525_000 - 1),
        0.16: SalesRange(320_000, 400_000 - 1),
        0.14: SalesRange(240_000, 400_000 - 1),
        0.12: SalesRange(150_000, 240_000 - 1),
        0.10: SalesRange(0, 150_000 - 1),
    }
    comp_brackets = [
        CommissionBracket(rate=rate, sales_range=sales_range)
        for rate, sales_range in ranges.items()
    ]
    return sum(bracket.sales_bonus(total_sales) for bracket in comp_brackets)


def main() -> None:
    # try:
    #     total_income = int(sys.argv[1])
    # except ValueError:
    #     print(f"{sys.argv[1]} is not a valid number for calculating a commission.")
    #     exit(1)
    # total_commission = get_bonus_from_total_sales(total_income)
    # print(f"Total commission: ${total_commission:,.2f}")

    # Generate sales data
    sales_data = range(0, 1000000, 10000)
    bonuses = [get_bonus_from_total_sales(sales) for sales in sales_data]
    # Plotting the data
    plt.figure(figsize=(10, 6))
    plt.plot(sales_data, bonuses, marker="o")
    plt.title("Relationship between Total Sales and Bonuses")
    plt.xlabel("Total Sales")
    plt.ylabel("Bonus")
    plt.grid(True)
    plt.autoscale(True)
    plt.show()


if __name__ == "__main__":
    main()
