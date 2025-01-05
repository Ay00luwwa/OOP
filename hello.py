class ShoppingBot:
    def __init__(self):
        self.cart = []

    def add_to_cart(self, item):
        self.cart.append(item)
        print(f"{item} has been added to your cart.")

    def remove_from_cart(self, item):
        if item in self.cart:
            self.cart.remove(item)
            print(f"{item} has been removed from your cart.")
        else:
            print(f"{item} is not in your cart.")

    def view_cart(self):
        if self.cart:
            print("Your cart contains:")
            for item in self.cart:
                print(f"- {item}")
        else:
            print("Your cart is empty.")

    def checkout(self):
        if self.cart:
            print("Checking out the following items:")
            for item in self.cart:
                print(f"- {item}")
            self.cart.clear()
            print("Thank you for your purchase!")
        else:
            print("Your cart is empty. Add items to your cart before checking out.")

if __name__ == "__main__":
    bot = ShoppingBot()
    while True:
        print("\nOptions:")
        print("1. Add to cart")
        print("2. Remove from cart")
        print("3. View cart")
        print("4. Checkout")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            item = input("Enter the item to add: ")
            bot.add_to_cart(item)
        elif choice == "2":
            item = input("Enter the item to remove: ")
            bot.remove_from_cart(item)
        elif choice == "3":
            bot.view_cart()
        elif choice == "4":
            bot.checkout()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")