# inheritance: child class extends and specialises a parent

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def greet(self):
        return f"Hello, {self.username}"

    def can_delete(self):
        return False


class AdminUser(User):
    def __init__(self, username, email, department):
        super().__init__(username, email)   # reuse parent __init__
        self.department = department

    def greet(self):
        return f"{super().greet()} [Admin · {self.department}]"  # extend, not replace

    def can_delete(self):
        return True


user = User("alice", "alice@example.com")
admin = AdminUser("bob", "bob@example.com", "Engineering")

print(user.greet())
print(admin.greet())

print(user.can_delete())
print(admin.can_delete())

print(isinstance(admin, User))
print(isinstance(user, AdminUser))
