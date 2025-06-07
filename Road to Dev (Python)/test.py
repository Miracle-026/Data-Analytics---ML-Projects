username = input("Enter username: ")
print("Welcome to Zara stores " + username)
print("What would you like to buy?")
catalog = list(("Nike shoes", "Adidas shorts", "Louis Vuitton shirts", "Dior caps", "Rolex watches"))
print(catalog)
order = input("")
if "Nike shoes" in order:
    print("Which size?")
    print([40, 42, 44, 45])
    order1 = input()
    print("Do you want to confirm this purchase?")
    confirmation = input("")
    if "yes" in confirmation:
        print("Your order has been confirmed. \nThank you for shopping with us.\nDelivery in two minutes")

if "Adidas shorts" in order:
    print("Which size?")
    print([36, 38, 40, 42])
    order1 = input()
    print("Do you want to confirm this purchase?")
    confirmation = input("")
    if "yes" in confirmation:
        print("Your order has been confirmed. \nThank you for shopping with us.\nDelivery in two minutes")

if "Louis Vuitton shirts" in order:
    print("Which size?")
    print(["S", "M", "L", "XL"])
    order1 = input()
    print("Do you want to confirm this purchase?")
    confirmation = input("")
    if "yes" in confirmation:
        print("Your order has been confirmed. \nThank you for shopping with us.\nDelivery in two minutes")

if "Dior caps" in order:
    print("Which size?")
    print([40, 42, 44, 45])
    order1 = input()
    print("Do you want to confirm this purchase?")
    confirmation = input("")
    if "yes" in confirmation:
        print("Your order has been confirmed. \nThank you for shopping with us.\nDelivery in two minutes")

if "Rolex watch" in order:
    print("Do you want to confirm this purchase?")
    confirmation = input("")
    if "yes" in confirmation:
        print("Your order has been confirmed. \nThank you for shopping with us.\nDelivery in two minutes")
