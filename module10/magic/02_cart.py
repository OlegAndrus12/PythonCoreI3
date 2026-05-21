class CartItem:
    def __init__(self, name, price, qty=1):
        self.name = name
        self.price = price
        self.qty = qty

    def __repr__(self):
        return f"{self.name} x{self.qty} @ ${self.price:.2f}"


class ShoppingCart:
    def __init__(self):
        self._items = []

    def __len__(self):
        return sum(item.qty for item in self._items)

    def __contains__(self, name):
        return any(item.name == name for item in self._items)

    def __getitem__(self, index):
        return self._items[index]

    def __iter__(self):
        return iter(self._items)

    def __iadd__(self, item):
        for existing in self._items:
            if existing.name == item.name:
                existing.qty += item.qty
                return self
        self._items.append(item)
        return self

    def __bool__(self):
        return len(self._items) > 0

    def __str__(self):
        if not self:
            return "Cart is empty"
        lines = [str(item) for item in self._items]
        total = sum(item.price * item.qty for item in self._items)
        lines.append(f"─" * 30)
        lines.append(f"Total: ${total:.2f}")
        return "\n".join(lines)


cart = ShoppingCart()
print(f"Empty cart: {bool(cart)}")          # False

cart += CartItem("Apple", 0.99, 3)
cart += CartItem("Bread", 2.49)
cart += CartItem("Apple", 0.99, 2)          # merges with existing Apple

print(f"Items in cart: {len(cart)}")        # 6
print(f"Has Bread: {'Bread' in cart}")      # True
print(f"Has Milk: {'Milk' in cart}")        # False
print(f"First item: {cart[0]}")             # Apple x5 @ $0.99
print()
print(cart)
