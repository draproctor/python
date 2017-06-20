def tax_calc(income):
    income = float(income)
    first_bracket = income - (0.10 * income)
    second_bracket = income - (932 + 0.15 * (income - 9325))
    third_bracket = income - (5226 + 0.25 * (income - 37950))
    fourth_bracket = income - (18713 + 0.28 * (income - 91900))
    fifth_bracket = income - (46643 + 0.33 * (income - 191650))
    sixth_bracket = income - (120910 + 0.35 * (income - 416700))
    seventh_bracket = income - (121505 + 0.396 * (income - 418400))
    if income < 9325:
        return first_bracket
    elif income > 9326 and income < 37950:
        return second_bracket
    elif income > 37951 and income < 91900:
        return third_bracket
    elif income > 91901 and income < 191650:
        return fourth_bracket
    elif income > 191651 and income < 416700:
        return fifth_bracket
    elif income > 416701 and income < 418400:
        return sixth_bracket
    elif income > 418400:
        return seventh_bracket
    else:
        print 'Invalid integer entered. Please try again.'

def paycheck_info(post_tax):
    return post_tax / 26

def monthly_info(post_tax):
    return post_tax / 12

def max_rent_info(monthly):
    return monthly / 3

def mo_post_rent(monthly,rent):
    return monthly - rent

def mo_all_bills(monthly,rent,bills):
    return monthly - rent - bills

income = float(raw_input("What's your yearly income?\n"))
rent = float(raw_input("What's your current monthly rent?\n"))
bills = float(raw_input("What's your current misc. bills per month?\n"))

post_tax = tax_calc(income)
pc = paycheck_info(post_tax)
mi = monthly_info(post_tax)
mri = max_rent_info(mi)
mpr = mo_post_rent(mi, rent)
mab = mo_all_bills(mi, rent, bills)

print "%f is earned each year after taxes." % (post_tax)
print "%f is the maximum rent that can be paid." % (mri)
print "%f is earned per paycheck." % (pc)
print "%f is earned per month." % (mi)
print "%f is earned per month after all bills." % (mpr)
