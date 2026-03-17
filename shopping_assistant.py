def calculate_discount(price, discount_percent):
    if discount_percent < 0 or discount_percent > 100:
        return "Invalid discount"
    discount = (discount_percent / 100) * price
    return round(price - discount, 2)

def compare_prices(price1, price2):
    if price1 < price2:
        return "Product 1 is cheaper"
    elif price2 < price1:
        return "Product 2 is cheaper"
    else:
        return "Both are equal"

def is_good_deal(price, original_price):
    if original_price == 0:
        return "Invalid price"
    discount = ((original_price - price) / original_price) * 100
    if discount >= 20:
        return "Good deal"
    else:
        return "Not a good deal"

def apply_coupon(price, coupon_code):
    coupons = {
        "SAVE10": 10,
        "SAVE20": 20,
        "SAVE50": 50
    }
    if coupon_code in coupons:
        return calculate_discount(price, coupons[coupon_code])
    return "Invalid coupon"
