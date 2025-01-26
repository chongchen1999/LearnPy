class Item:
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total(self) -> float:
        """Calculates the total cost of this item."""
        return self.price * self.quantity

    def __str__(self):
        return f"{self.name}: ${self.price:.2f} x {self.quantity} = ${self.calculate_total():.2f}"


class Cart:
    def __init__(self):
        self.items = []  # Composition: Cart is composed of Item objects.

    def add_item(self, item: Item):
        """Adds an item to the cart."""
        self.items.append(item)

    def calculate_total(self) -> float:
        """Calculates the total cost of all items in the cart."""
        return sum(item.calculate_total() for item in self.items)

    def __str__(self):
        if not self.items:
            return "Your cart is empty."
        cart_content = "\n".join(str(item) for item in self.items)
        return f"Cart Contents:\n{cart_content}\nTotal: ${self.calculate_total():.2f}"


# Demonstrating Combination
def main():
    # Create items
    item1 = Item("Laptop", 1200.00, 1)
    item2 = Item("Mouse", 25.50, 2)
    item3 = Item("Keyboard", 75.00, 1)

    # Create cart and add items
    cart = Cart()
    cart.add_item(item1)
    cart.add_item(item2)
    cart.add_item(item3)

    # Print cart details
    print(cart)


if __name__ == "__main__":
    main()
