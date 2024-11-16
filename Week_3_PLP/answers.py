def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_price = (discount_percent/100) * price
        final_price = price - discount_price
        return final_price
    else:
        return price
    
try:
    original_price = float(input("Enter original price: "))
    discount_percentage = float(input("Enter discount percentage: "))

    # Calculate and display the result
    final_price = calculate_discount(original_price, discount_percentage)
    if final_price < original_price:
        print(f"Final price after discount is: {final_price:.2f}")
    else:
        print(f"No discount applied. Original price: {original_price:.2f}")
except ValueError:
    print("Please enter price and discount.")