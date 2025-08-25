#assignments
def calculate_discount(price, discount_percentage):
    if discount_percentage >= 20:
        discount_amount = price * (discount_percentage / 100)
        final_price= price - discount_amount
        return final_price
    else:
        return price
print(calculate_discount(100, 20))
