def income_remaining(income):
    # Convert to float for proper calculations
    income = float(income)

    # First tax bracket
    if income <= 9525:
        return income - (0.10 * income)
    # Second tax bracket
    elif income > 9326 and income <= 38700:
        return income - (952.50 + 0.12 * (income - 9525))
    # Third tax bracket
    elif income > 38701 and income <= 82500:
        return income - (4453.50 + 0.22 * (income - 38700))
    # Fourth tax bracket
    elif income > 82501 and income <= 157_500:
        return income - (14089.50 + 0.24 * (income - 82500))
    # Fifth tax bracket
    elif income > 157_501 and income <= 200_000:
        return income - (32089.50 + 0.32 * (income - 157_500))
    # Sixth tax bracket
    elif income > 200_001 and income <= 500_000:
        return income - (45689.50 + 0.35 * (income - 200_000))
    # Seventh tax bracket
    elif income > 500_001:
        return income - (150_689.50 + 0.37 * (income - 500_000))
    else:
        print("Invalid value entered. Please try again.")


def tax_bonuses(bonus):
    return float(bonus) / 2


def paycheck_info(post_tax):
    return post_tax / 26


def info_monthly(post_tax):
    return post_tax / 12


def info_max_rent(monthly):
    return monthly / 3


def mo_post_rent(monthly, rent):
    return monthly - rent


def mo_all_bills(monthly, rent, bills):
    return monthly - rent - bills


income = input("What is your yearly income?\n")
bonus = input("How much did you earn in bonuses for the year?\n")
rent = float(input("What is your current monthly rent?\n"))
bills = float(input("What is your current misc. bills per month?\n"))

post_tax = income_remaining(income) + tax_bonuses(bonus)
pc = paycheck_info(post_tax)
mi = info_monthly(post_tax)
mri = info_max_rent(mi)
mpr = mo_post_rent(mi, rent)
mab = mo_all_bills(mi, rent, bills)

print(f"{round(post_tax, 2)} is earned each year after taxes.")
print(f"{round(mri, 2)} is the maximum rent that can be paid.")
print(f"{round(pc, 2)} is earned per paycheck.")
print(f"{round(mi, 2)} is earned per month.")
print(f"{round(mpr, 2)} is earned per month after all bills.")
