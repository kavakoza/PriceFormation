def total_price(price):

    """Total price calculation with taxes and commissions"""

    tax = price * 0.06
    bank_commission = price * 0.02
    seller_commission = price * 0.02
    marketplace_commission = price * 0.20

    final_price = price + tax + bank_commission + seller_commission + marketplace_commission

    return final_price
