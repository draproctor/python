import sys
from dataclasses import dataclass

from matplotlib import pyplot


@dataclass
class CommissionBracket:
    rate: float
    sales_range: range

    def sales_bonus(self, sales: float | int) -> float:
        if sales < self.sales_range.start:
            return 0.0
        # A bracket only applies to the maximum amount of sales in its range.
        sales = min(sales, self.sales_range.stop)
        bonus = self.rate * (sales - self.sales_range.start)
        print(f"{self.rate} * ({sales} - {self.sales_range.start}) = ${bonus:,.2f}")
        return bonus


class IncomeTracker:
    brackets: list[CommissionBracket]

    def __init__(self) -> None:
        ranges = {
            0.28: range(600_000, sys.maxsize),
            0.21: range(525_000, 600_000),
            0.19: range(400_000, 525_000),
            0.16: range(320_000, 400_000),
            0.14: range(240_000, 400_000),
            0.12: range(150_000, 240_000),
            0.10: range(0, 150_000),
        }
        self.brackets = [
            CommissionBracket(rate=rate, sales_range=sales_range)
            for rate, sales_range in ranges.items()
        ]

    def total_bonus(self, total_sales: int) -> float:
        return sum(bracket.sales_bonus(total_sales) for bracket in self.brackets)


def main() -> None:
    tracker = IncomeTracker()
    sales_data = range(0, 1000000, 10000)
    bonuses = [tracker.total_bonus(sales) for sales in sales_data]

    pyplot.figure(figsize=(10, 6))
    pyplot.plot(sales_data, bonuses)
    pyplot.title("Relationship between Total Sales and Bonuses")
    pyplot.xlabel("Total Sales")
    pyplot.ylabel("Bonus")
    pyplot.grid(True)
    pyplot.autoscale(True)
    pyplot.show()


if __name__ == "__main__":
    main()
