import uuid


class BankAccount:
    _INTEREST_TIERS = [
        (100_000, 0.05),
        (10_000,  0.03),
        (0,       0.01),
    ]

    def __init__(self, owner, initial_balance=0):
        self._id = str(uuid.uuid4())[:8].upper()
        self._owner = owner
        self._balance = 0
        self.balance = initial_balance  # triggers setter

    @property
    def account_id(self):
        return self._id

    @property
    def owner(self):
        return self._owner

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = round(amount, 2)

    @property
    def interest_rate(self):
        for threshold, rate in self._INTEREST_TIERS:
            if self._balance >= threshold:
                return rate

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal must be positive")
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount

    def __str__(self):
        return (
            f"Account {self._id} [{self._owner}]: "
            f"${self._balance:,.2f}  (rate: {self.interest_rate * 100:.0f}%)"
        )

    def __repr__(self):
        return f"BankAccount(id={self._id!r}, owner={self._owner!r}, balance={self._balance})"


acc = BankAccount("Alice", 5_000)
print(acc)

acc.deposit(200)
acc.withdraw(100)
print(f"Balance: ${acc.balance:,.2f}")
print(f"Interest rate: {acc.interest_rate * 100:.0f}%")

premium = BankAccount("Bob", 150_000)
print(premium)

try:
    acc.withdraw(50_000)
except ValueError as e:
    print(e)

try:
    BankAccount("Eve", -100)
except ValueError as e:
    print(e)
