def validate_password(password):
    rules = [
        any(c.isupper() for c in password),
        any(c.islower() for c in password),
        any(c.isdigit() for c in password),
        len(password) >= 8,
    ]
    return all(rules)

print(validate_password("Secure1!"))
print(validate_password("weakpass"))
print(validate_password("NOLOWER1"))

form = {"name": "Alice", "email": "alice@mail.com", "age": "28"}
required = ["name", "email", "age"]

all_filled = all(form.get(field) for field in required)
print(f"Form complete: {all_filled}")

cart = [
    {"item": "book", "in_stock": True},
    {"item": "pen", "in_stock": False},
    {"item": "notebook", "in_stock": True},
]

has_out_of_stock = any(not item["in_stock"] for item in cart)
print(f"Has out-of-stock items: {has_out_of_stock}")

permissions = ["read", "write", "delete"]
required_perms = ["read", "write"]
dangerous_perms = ["delete", "admin"]

can_proceed = all(p in permissions for p in required_perms)
is_dangerous = any(p in permissions for p in dangerous_perms)

print(f"Can proceed: {can_proceed}")
print(f"Is dangerous: {is_dangerous}")
