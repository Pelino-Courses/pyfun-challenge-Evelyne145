
class Product:
    """
    A class to represent a product in an inventory system.

    Attributes:
        name (str): What the product is called.
        price (float): How much the product costs.
        quantity (int): How many units are in stock.

    You can:
    - Update the price
    - Add or remove stock
    - Check the total value of the product in stock

    Example:
        >>> product = Product("Notebook", 5.99, 20)
        >>> product.add_stock(5)
        >>> product.remove_stock(3)
        >>> print(product.get_total_value())
        137.77
    """

    def __init__(self, name: str, price: float, quantity: int = 0):
        """
        Let's set up the product with a name, a price, and a starting quantity.

        Raises:
            ValueError: If anything looks off (like a negative price or quantity).
        """
        if not name or not isinstance(name, str):
            raise ValueError("Hey! The product name must be a non-empty string.")
        if price <= 0:
            raise ValueError("Hmm... price should be more than zero.")
        if quantity < 0:
            raise ValueError("Quantity can't be negative. You can't start with less than 0!")

        self.__name = name
        self.__price = price
        self.__quantity = quantity

    # Read-only access using encapsulation (can't directly change these outside the class)
    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @property
    def quantity(self):
        return self.__quantity

    def update_price(self, new_price: float):
        """Update the price — it must be positive."""
        if new_price <= 0:
            raise ValueError("The new price must be greater than zero.")
        self.__price = new_price

    def add_stock(self, amount: int):
        """Add more stock (it must be a positive number)."""
        if amount <= 0:
            raise ValueError("You can only add a positive number of items.")
        self.__quantity += amount

    def remove_stock(self, amount: int):
        """
        Remove some items from stock — but only if you have enough!

        Raises:
            ValueError: If you're trying to remove more than what's available.
        """
        if amount <= 0:
            raise ValueError("You can only remove a positive number of items.")
        if amount > self.__quantity:
            raise ValueError(f"Not enough stock to remove {amount} items. You only have {self.__quantity}.")
        self.__quantity -= amount

    def get_total_value(self) -> float:
        """How much is all this stock worth right now?"""
        return round(self.__price * self.__quantity, 2)

    def __str__(self):
        return f"{self.__name} | ${self.__price:.2f} | In stock: {self.__quantity}"


# 👇 Let's test it out — only runs when you run this file directly
if __name__ == "__main__":
    try:
        print("📦 Creating a new product...")
        keyboard = Product("Mechanical Keyboard", 99.99, 15)
        print(keyboard)

        print("\n💰 Updating the price...")
        keyboard.update_price(89.99)
        print(keyboard)

        print("\n➕ Adding stock...")
        keyboard.add_stock(10)
        print(keyboard)

        print("\n➖ Removing some stock...")
        keyboard.remove_stock(5)
        print(keyboard)

        print("\n📊 Total value of stock:")
        print(f"${keyboard.get_total_value()}")

        # Uncomment to see error handling in action
        # keyboard.remove_stock(100)  # Will raise an error
        # bad_product = Product("", -5, -10)  # Will raise an error

    except Exception as e:
        print(f"\n❌ Oops! Something went wrong: {e}")
        