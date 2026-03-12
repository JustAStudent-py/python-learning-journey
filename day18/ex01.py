print("\n=== Product Price Calculator ===")
print("Enter the product price and discount code.")
print("Type 0 as the price to exit.\n")

while True:
    # Ask the user to enter the product price and discount code
    price, discount_code = input("Price and discount (Y/N): ").split()

    # Convert price to float
    price = float(price)

    # Exit condition
    if price == 0:
        print("\nProgram terminated.")
        break

    # Normalize the discount code
    discount_code = discount_code.upper()

    # Apply discount if code is Y
    if discount_code == "Y":
        final_price = price * 0.9
        print(f"Final price with discount: ${final_price:.2f}")
    else:
        print(f"Final price: ${price:.2f}")

    print("-" * 35)