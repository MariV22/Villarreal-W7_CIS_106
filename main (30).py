def compute_total(quantity, price):
    total = quantity * price
    if total > 100000.00:  # Check if the total exceeds $100,000.00 for discount
        total *= 0.9  # Apply a 10% discount
    return total

def main():
    extended_price = 0
    print("Enter the quantity and price (press Ctrl+Z to stop):")

    while True:
        try:
            quantity = float(input("Quantity: "))
            price = float(input("Price: "))
            total = compute_total(quantity, price)
            extended_price += total

            print(f"Quantity: {quantity}, Price: {price}, Total: {total:.2f}")
        except EOFError:
            print("\nInput stopped.")
            break

    print(f"Extended Price: {extended_price:.2f}")

if __name__ == "__main__":
    main()