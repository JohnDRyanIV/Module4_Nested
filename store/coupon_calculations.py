from decimal import *


def calculate_price(price, cash_coupon, percentage_coupon):
    getcontext().prec = 20
    total = price - cash_coupon  # Applying cash coupon discount
    total = total - (total * Decimal((percentage_coupon / 100)))  # Applying percentage discount
    tax = Decimal(total) * Decimal(.06)  # Calculating tax
    # Adding shipping cost
    if total < 10:
        total = Decimal(total) + Decimal(5.95)

    # Setting precision so that total is returned with proper number of decimal places
    precision = 2
    i = 1
    while i < total:  # While loop determines precision necessary for proper decimal places
        i = i * 10
        precision = precision + 1

    getcontext().prec = precision
    total = Decimal(total) + Decimal(tax)
    # Converting to float so other programs don't have to import decimal class
    total = float(total)

    return total


if __name__ == '__main__':
    pass
