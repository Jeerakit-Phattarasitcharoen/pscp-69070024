"""Bill"""
def main():
    """Bill"""
    price = int(input())
    service = 0
    if price * (10 / 100) < 50:
        service = 50
    elif price * (10 / 100) > 1000:
        service = 1000
    else:
        service = price * (10 / 100)
    all_price = (price + service) * (7 / 100)
    total = price + service + all_price
    print(f"{total:.2f}")
main()
