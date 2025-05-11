class Product:
    def __init__(self, price):
        self._price = price  # Private attribute

    @property
    def price(self):
        """Getter for the price."""
        print("Getting the price")
        return self._price

    @price.setter
    def price(self, value):
        """Setter for the price."""
        if value < 0:
            print("Price cannot be negative.")
        else:
            print("Setting the price")
            self._price = value

    @price.deleter
    def price(self):
        """Deleter for the price."""
        print("Deleting the price")
        del self._price

# Example usage:
product = Product(100)  # Create a Product object with initial price 100

# Accessing the price using the getter
print(product.price)  # Output: Getting the price \n 100

# Updating the price using the setter
product.price = 150  # Output: Setting the price
print(product.price)  # Output: Getting the price \n 150

# Trying to set a negative price (invalid)
product.price = -50  # Output: Price cannot be negative.

# Deleting the price using the deleter
del product.price  # Output: Deleting the price
