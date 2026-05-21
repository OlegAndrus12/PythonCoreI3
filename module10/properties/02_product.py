class Product:
    def __init__(self, name, price, discount=0):
        self._name = name
        self.price = price       # uses setter
        self.discount = discount  # uses setter

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = round(value, 2)

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        if not 0 <= value <= 100:
            raise ValueError("Discount must be between 0 and 100")
        self._discount = value

    @property
    def final_price(self):
        return round(self._price * (1 - self._discount / 100), 2)

    @property
    def is_on_sale(self):
        return self._discount > 0

    def __str__(self):
        if self.is_on_sale:
            return (
                f"{self._name}: ${self._price:.2f} → ${self.final_price:.2f} "
                f"({self._discount}% off)"
            )
        return f"{self._name}: ${self._price:.2f}"

    def __repr__(self):
        return f"Product({self._name!r}, price={self._price}, discount={self._discount})"


laptop = Product("Laptop", 1299.99)
print(laptop)               # Laptop: $1299.99

laptop.discount = 15
print(laptop)               # Laptop: $1299.99 → $1104.99 (15% off)
print(f"On sale: {laptop.is_on_sale}")

headphones = Product("Headphones", 249.00, discount=20)
print(headphones)

catalog = [
    Product("Keyboard", 89.00),
    Product("Monitor", 499.00, discount=10),
    Product("Mouse", 39.00, discount=5),
]

print("\nSale items:")
for item in filter(lambda p: p.is_on_sale, catalog):
    print(f"  {item}")

try:
    laptop.discount = 110
except ValueError as e:
    print(e)
